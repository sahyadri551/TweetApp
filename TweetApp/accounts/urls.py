from django.urls import path
from .views import profile_edit, register, profile, toggle_follow, followers_list, following_list

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("follow/<str:username>/",toggle_follow,name="toggle_follow"),
    path("user/<str:username>/followers/",followers_list,name="followers_list"),
    path("user/<str:username>/following/",following_list,name="following_list"),
]