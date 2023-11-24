
from django.shortcuts import HttpResponse


def register(request):
    """View function for registration app home page."""
    return HttpResponse("Hello, world. You're at the registration app home page.")

