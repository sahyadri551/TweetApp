
from django import forms
from .models import Tweet, Comment

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text","image",]

        widgets = { # type: ignore
            "text": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What's happening?",
                    "class": "w-full rounded-xl border border-slate-300 p-3 focus:outline-none focus:ring-2 focus:ring-slate-400"
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "w-full border border-slate-300 p-3 focus:outline-none focus:ring-2 focus:ring-slate-400"
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 2,
                    "placeholder": "Write a comment..."})}