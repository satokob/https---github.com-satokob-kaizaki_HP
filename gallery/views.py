from django.shortcuts import render
from django.http import HttpResponse

def gallery(request):
    return render(request, 'gallery/gallery.html')

