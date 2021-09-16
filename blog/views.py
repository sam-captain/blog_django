import contextlib
from typing import ContextManager
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Feedback

# Create your views here.    
def home(request):
    Context = {
        'heading' : 'Welcome to my Landing page',
         'services' : Category.objects.all()[:3],
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

def dashboard(request):
    Context ={}
    
    return render(request,'blog/admin/dashboard.html',Context)


def saveFeedback(request):
    name =request.POST.get("name")
    email =request.POST.get("email")
    number =request.POST.get("number")
    message = request.POST.get("message")
    Feedback.objects.create(name= name, email=email, phone_number=number, message=message)

    context ={}
    return HttpResponseRedirect('/contact')

def showFeedback(request):
    context ={}
    context['feedback_list'] = Feedback.objects.all()
    return render(request, "blog/admin/Feedback.html", context)


def showCategories(request):
    context = {
        'category_list': Category.objects.all()
    }
    return render(request, "blog/admin/categories.html", context)

def categoryForm(request):
    context ={}
    return render(request, "blog/admin/category-form.html", context)

def storeCategory(request):
    Category_name = request.POST.get("name")

    Category.objects.create(name= Category_name)

    return HttpResponseRedirect ("/staff/categories")

def deleteCategory(request, id):
    our_category = Category.objects.get(pk=id)
    our_category.delete()
    return HttpResponseRedirect('/staff/categories')


   



