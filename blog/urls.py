
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('<str:slug>',views.blog,name='blog'),
    path('<str:top_slug>',views.top_posts,name='top_blog')
]
