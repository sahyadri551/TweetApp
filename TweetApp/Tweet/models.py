from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at', '-modified_at']

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"
    
class Comment(models.Model):
    tweet = models.ForeignKey("Tweet.Tweet",on_delete=models.CASCADE,related_name="comments") # type: ignore
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    text = models.TextField( max_length=500)
    created_at = models.DateTimeField( auto_now_add=True)
    modified_at = models.DateTimeField( auto_now=True)

    class Meta:
        ordering = ["-created_at", "-modified_at"]

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"
    
