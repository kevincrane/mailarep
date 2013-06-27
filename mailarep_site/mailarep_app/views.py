from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """ Home page of the web site
    """
    return render(request, 'index.html')

def writeletter(request):
    """ Form page to write a letter
    """
    return render(request, 'writeletter.html')


def leaderboard(request):
    """ Home page of the web site
    """
    return render(request, 'leaderboard.html')


# Custom view for a 404 error
#TODO: make views for both error types
def no_page_404_view(request):
    response = "<!DOCTYPE HTML>\n<html><body><h1>I couldn't find your page.</h1>" \
               "<h3>That makes me a very sad president. :(</h3></body></html>"
    return HttpResponse(response)


# Custom view for a 500 error
def server_error_500_view(request):
    response = "<!DOCTYPE HTML>\n<html><body><h1>Something bad happened to the server.</h1>" \
               "<h3>That fillibustered my heart. :(</h3></body></html>"
    return HttpResponse(response)
