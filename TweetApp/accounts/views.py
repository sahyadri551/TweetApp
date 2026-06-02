from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required
from Tweet.models import Tweet


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

    tweets = Tweet.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request,"registration/profile.html", {"tweets": tweets})