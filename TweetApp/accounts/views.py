from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegisterForm
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required
from Tweet.models import Tweet
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Follow

def register(request:HttpRequest)->HttpResponse: 
    if request.method == "POST": 
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm() 
    return render(request,"registration/register.html",{"form": form}) 

@login_required
def profile(request:HttpRequest)->HttpResponse:
    profile = request.user.profile # type: ignore
    tweets = Tweet.objects.filter(
        user=request.user
    ).order_by("-created_at")
    tweet_count = tweets.count()
    return render(request,"registration/profile.html", {"tweets": tweets, "profile": profile, "tweet_count": tweet_count})

@login_required
def profile_edit(request:HttpRequest)->HttpResponse:
    profile = request.user.profile # type: ignore
    if request.method == "POST":
        form = ProfileForm( request.POST, request.FILES,instance=profile) # type: ignore
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile) # type: ignore
    return render( request,"registration/profile_edit.html",{"form": form})

@login_required
def toggle_follow(request:HttpRequest, username:str)->HttpResponse:
    target_user = get_object_or_404(User,username=username)
    if target_user == request.user:
        return redirect("user_profile",username=username)
    follow = Follow.objects.filter(follower=request.user,following=target_user)
    if follow.exists():
        follow.delete()
    else:
        Follow.objects.create(follower=request.user,following=target_user)

    return redirect("user_profile",username=username)

def followers_list(request:HttpRequest, username:str)->HttpResponse:
    profile_user = get_object_or_404(User,username=username)
    followers = Follow.objects.filter(following=profile_user).select_related("follower")
    return render(request,"followers_list.html",{"profile_user": profile_user, "followers": followers,})

def following_list(request:HttpRequest, username:str)->HttpResponse:
    profile_user = get_object_or_404(User,username=username)
    following = Follow.objects.filter(follower=profile_user).select_related("following")
    return render(request,"following_list.html",{"profile_user": profile_user,"following": following,})