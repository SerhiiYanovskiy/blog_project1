"""blog_project URL Configuration

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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from blog_app.views import *

urlpatterns = [
    path('', PostList.as_view(), name='homepage'),
    path('post/<slug>', PostDetails.as_view(), name='post_details'),
    path('app/user-posts', login_required(UserPostList.as_view()), name='user_posts'),
    path('app/user-posts/add', login_required(CreatePost.as_view()), name='post_add'),
    path('app/user-posts/<slug>', login_required(UserPostDetails.as_view()), name='user_post_details'),
    path('app/user-posts/<slug>/update', login_required(UpdatePost.as_view()), name='post_update'),
    path('app/user-posts/<slug>/delete', login_required(DeletePost.as_view()), name='post_delete'),
    path('app/admin', admin.site.urls),
    path('app/login', UserLoginView.as_view(), name='login'),
    path('app/register', UserCreateView.as_view(), name='register'),
    path('app/logout', UserLogoutView.as_view(), name='logout'),
]
