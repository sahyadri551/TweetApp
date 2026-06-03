from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required
from Tweet.models import Tweet
from .forms import ProfileForm


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

    return render(request,"registration/profile.html", {"tweets": tweets, "profile": profile})

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