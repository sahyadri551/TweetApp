from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # type: ignore
    list_display = (
        "user",
        "bio",
        "created_at",
        "modified_at",
        "avatar",
        "dob",
        "nationality",
        "address",
        "mobile",
        "url",
        "profession",
    )