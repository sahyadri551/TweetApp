from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CommentForm, TweetForm
from .models import Tweet

def home(request:HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "index.html", {"tweets": tweets})

@login_required
def tweet_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("home")
    else:
        form = TweetForm()
    return render(request,"tweet_form.html",{"form": form})

def tweet_edit(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TweetForm(instance=tweet)
    return render( request,"tweet_form.html",{"form": form})

def tweet_delete(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("home")
    return render(request,"tweet_confirm_delete.html",{"tweet": tweet})

def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    profile_user = get_object_or_404(User,username=username)
    tweets = Tweet.objects.filter(user=profile_user).order_by("-created_at")
    tweet_count = tweets.count()
    return render(request,"user_profile.html",
            {"profile_user": profile_user,"tweets": tweets,"tweet_count": tweet_count,})

@login_required
def comment_create(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tweet = tweet
            comment.save()
    return redirect("home")