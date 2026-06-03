from django.urls import path
from .views import comment_create, home, tweet_create, tweet_edit, tweet_delete, user_profile

urlpatterns = [
    path("", home, name="home"),
    path("create/", tweet_create, name="tweet_create"),
    path("edit/<int:tweet_id>/", tweet_edit, name="tweet_edit"),
    path("delete/<int:tweet_id>/", tweet_delete, name="tweet_delete"),
    path("user/<str:username>/", user_profile, name="user_profile"),
    path("comment/<int:tweet_id>/",comment_create,name="comment_create"),
]
