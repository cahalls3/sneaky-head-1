from django.http import HttpResponse



# displays posts from other people
def indexPageView(requests):
    return HttpResponse('Home Page')


# displays all posts by user and provides a place for the user to share, update,
# and delete posts
def profilePageView(request):
    return HttpResponse('Profile Page')
