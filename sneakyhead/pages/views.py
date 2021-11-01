from django.http import HttpResponse


# displays either login page or user home page depending on if user is logged in
def indexPageView(request):
    return HttpResponse('Index Page')


# displays form to login or create profile
def loginPageView(request):
    return HttpResponse('Login Page')


# displays posts from other people
def homePageView(requests):
    return HttpResponse('Home Page')


# displays all posts by user and provides a place for the user to share, update,
# and delete posts
def profilePageView(request):
    return HttpResponse('Profile Page')
