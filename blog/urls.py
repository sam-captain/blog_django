"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django_blog.blog.models import Feedback
from django.contrib import admin
from django.urls import include, path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from blog import views

from .views import PostCreate, PostDetails, PostUpdateView, getCategoryPost, postList,PostDeleteView, saveComment, sendmail

staff_patterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('feedback', views.showFeedback, name="feedback"),
    path('save/faeedback', views.saveFeedback, name="save_feedback"),
    path('categories', views.showCategories, name="categories"),
    path('category/form', views.categoryForm, name="add_category"),
    path('store/category', views.storeCategory, name="store_category"),
    path('delete/category/<id>', views.deleteCategory, name="delete_category"),
    path('dalete/feedback/<id>',views.deleteFeedback, name="delete_feedback"),
    path('posts', postList.as_view(), name="posts"),
    path('create/post', PostCreate.as_view(), name="add_post"),
    path('view/post/<pk>', PostDetails.as_view(), name="view_post"),
    path('update/post/<pk>', PostUpdateView.as_view(), name="update_post"),
    path('delete/post/<pk>', PostDeleteView.as_view(), name="delete_post"),
    path('send/mail', views.sendmail, name ='send_mail')
    
    
]

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('myposts',views.myposts, name="myposts"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('post/details/<id>', views.getPostDetails, name="post_details"),
    path('save/comment/<id>', views.saveComment, name ="save_comment"),
    path('posts/category/<id>', views.getCategoryPost, name="category_post"),
    path('search', views.searchPosts, name="search"),
    path('staff/', include(staff_patterns)),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

