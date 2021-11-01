from django.urls import path
from .views import indexPageView, profilePageView


urlpatterns = [
    path("", indexPageView, name="index"),
    path("profile/", profilePageView, name="profile"),
]

# Hi this is a test by Carson

# Second test