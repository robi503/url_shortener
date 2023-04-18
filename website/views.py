from django.shortcuts import render
from URLs.models import URL

def welcome(request):
    return render(request, "website/welcome.html", {"links": URL.objects.all()})


