from django.http import HttpResponse
from django.shortcuts import render


def homepage(request: HttpResponse) -> HttpResponse:
    """Render the home page."""
    return render(request, "home.html")


def about(request: HttpResponse) -> HttpResponse:
    """Render the about page."""
    return render(request, "about.html")


# retun HttpResponse("My about page.")
