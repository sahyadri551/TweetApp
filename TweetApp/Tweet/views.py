from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .forms import TweetForm
from .models import Tweet

def home(request:HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "index.html", {"tweets": tweets})

def tweet_create(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = User.objects.first()
            tweet.save()
            return redirect("home")

    else:
        form = TweetForm()

    return render(
        request,
        "tweet_form.html",
        {"form": form}
    )
