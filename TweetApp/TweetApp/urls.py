
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [ # type: ignore
    path("", include("Tweet.urls")),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("accounts.urls")),
    path(
        "login/",auth_views.LoginView.as_view( template_name="registration/login.html"),
        name="login"),
    path(
        "logout/",auth_views.LogoutView.as_view(),name="logout"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore
