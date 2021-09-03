import contextlib
from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.    
def home(request):
    Context = {
        'heading' : 'Welcome to my Landing page',
         'services' : ["coding", "eating", "sleeping"],
         'posts' : ["Big blue world","Out of space", "A-O-A-Okay"],
    }
    return render(request,"home.html", Context)

def contact(request):
    Context = {
        'number' : '2547256995129',
        'email' :'Samkent@gmail.com',
        'address': 'juja kiambu 02-40054',
        
    }
    return render(request,"contact.html", Context)

def blog(request):
    context = {
        'header' : 'Welcome to my blog posts',
        'posts' : ["Big blue world","Out of space", "A-O-A-Okay", "Seven greate planets","Nice water breeze","bubble honey bee"],
    }
    return render(request,"blog/blog.html", context)

def myposts(request):
    context = {
        'details' : ["Run a contest","Review books/products/films","Interview someone",],

    }
    return render(request,"post-details.html",context)

