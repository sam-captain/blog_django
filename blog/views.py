import contextlib
from typing import ContextManager
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Category, Comments, Feedback, Post, User
from  django.views.generic import ListView, DetailView
from  django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import CommentForm, mailform
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.    
def home(request):
    
    # num_of_visits = request.session.get("num_of_visits", 0)
    # request.session["num_of_visits"] = num_of_visits + 1

    Context = {
        'heading' : 'Welcome to my Landing page',
        'services' : Category.objects.all()[:8],
        'posts' : Post.objects.all()[:6],
        
    }
    return render(request,"home.html", Context)


def getPostDetails(request, id):

    our_post = Post.objects.get(pk = id)
    
    our_post.views += 1
    our_post.save()

    our_post.category.views += 1
    our_post.category.save()
    

    context ={
        'post' : our_post,
        'categories' : Category.objects.all(),
        'posts' : Post.objects.filter(category = our_post.category).exclude(pk=our_post.id),
        'commentForm': CommentForm(),
        'comments' : Comments.objects.filter(post = our_post.id)
    }

    return render(request, 'blog/post_details.html',context)

def saveComment(request, id):
    form = CommentForm(request.POST)
    redirect_url = "/posts/details/"+id

    if form.is_valid():
        name = form.cleaned_data['name',None]
        email = form.cleaned_data['email',None]
        phone_number = form.cleaned_data['phone_number',None]
        message = form.cleaned_data['message',None]

        user = User.objects.get(pk =1)
        post = Post.objects.get(pk =id)
        

        Comments.objects.create(message = message, user = user, post = post)

        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseRedirect(redirect_url)



def contact(request):
    Context = {
        'number' : '2547256995129',
        'email' :'Samkent@gmail.com',
        'address': 'juja kiambu 02-40054',
        
    }
    return render(request,"contact.html", Context)

def blog(request):
    context = {
        'posts' : Post.objects.all(),
        'all_categories' : Category.objects.all(),
        'title' : 'All you can find is in there'
    }
    return render(request,"blog/blog.html", context)

def myposts(request):
    context = {
        'details' : ["Run a contest","Review books/products/films","Interview someone",],

    }
    return render(request,"post-details.html",context)

@login_required
def dashboard(request):
    categories=Category.objects.all()
    posts = Post.objects.all()
    Feedbacks =Feedback.objects.all()
    Context ={

        'category_list':categories,
        'post_list' : posts,
        'feedback_list' : Feedbacks
    }
    
    return render(request,'blog/admin/dashboard.html',Context)

@csrf_exempt
def saveFeedback(request):
    name =request.POST.get("name",None)
    email =request.POST.get("email",None)
    number =request.POST.get("number", None)
    message = request.POST.get("message", None)
    Feedback.objects.create(name= name, email=email, phone_number=number, message=message)
    data  ={}
    return JsonResponse(data)

    context ={}
    return HttpResponseRedirect('/contact')
@login_required
def showFeedback(request):
    context ={}
    context['feedback_list'] = Feedback.objects.all()
    return render(request, "blog/admin/Feedback.html", context)

@login_required
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

def deleteFeedback(request, id):
    our_feedback= Feedback.objects.get(pk=id)

    our_feedback.delete()

    return HttpResponseRedirect('/staff/feedback')

class postList(LoginRequiredMixin, ListView):
    model = Post
    template_name ="blog/admin/post.html"


class PostCreate(CreateView):
    model = Post
    template_name ="blog/admin/post-form.html"
    fields = '__all__'
    success_url = '/staff/posts'

@method_decorator (login_required, name="dispatch")
class PostDetails(DetailView):
    model = Post
    success_url ='/staff/posts'
    fields = '__all__'
    template_name = "blog/admin/post_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] =  Comments.objects.filter(post = self.kwargs['pk']) 
        return context

class PostUpdateView(UpdateView):
    model = Post
    template_name ="blog/admin/post-form.html"
    fields = 'title','message','slug','category','user','keywords','image_url'
    success_url = '/staff/posts'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/staff/posts'
    template_name = 'blog/admin/post_delete.html'

def getCategoryPost(request, id):
    category = Category.objects.get(pk = id)
    posts = Post.objects.filter(category = category.id)

    category.views +=1
    category.post
    
    context ={
        'posts' : posts,
        'all_categories' : Category.objects.all(),
        'title' : "Post in the category :" +category.name

    }
    return render(request, 'blog/blog.html', context)

@csrf_exempt
def searchPosts(request):

    search = request.POST.get('searchInput')
    posts = Post.objects.filter(message__icontains = search).values()
    data = {
         'posts' : list(posts)
    }
    return JsonResponse(data)

def sendmail(request):
    if request.method == "POST":
        form = mailform(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']


            send_mail(
                subject,
                message,
                'samkent@gmail.com',
               [recipient],
               fail_silently = False
            )
            
            return HttpResponseRedirect('/staff/feedback')
    else:
            context ={
                'form' : mailform
            }
            return render(request, 'blog/admin/send_mail.html', context)
    


   



