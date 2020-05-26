from django.http import HttpResponse
from django.shortcuts import render
from gallery.models import Gallery
from gallery.models import Gallery
def home(request):

    gallary = Gallery.objects
    return render(request,'home.html',{'gallery':gallary})