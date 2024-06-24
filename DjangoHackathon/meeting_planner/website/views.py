# actual code for web page

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting, Room


# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context={}
    return render(request, "website/welcome.html", context)
# how does this work in the backend?


def about(request):
    return HttpResponse("<h1>Hi my name is Shashwat Ghevde</h1>")

