from django.urls import path
from .views import indexPageView, loginPageView, homePageView, profilePageView


urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),
    path("home/", homePageView, name="home"),
    path("profile/", profilePageView, name="profile")
]

# Hi this is a test by Carson

# Second test