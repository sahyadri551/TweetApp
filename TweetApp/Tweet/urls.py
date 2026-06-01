from django.urls import path
from .views import home, tweet_create

urlpatterns = [
    path("", home, name="home"),
    path("create/", tweet_create, name="tweet_create"),
]
