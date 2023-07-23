"""
URL configuration for blognet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , re_path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from blog import models
from django.views.static import serve

admin.site.site_header="technical realm admin panel by himanshu"
admin.site.site_title="technical realm admin panel"
admin.site.index_title="welcome to technical realm admin panel"

from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/search', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('about/search/', views.about, name='about'),
    # path('adminposting/', views.adminposting, name='adminposting'),
    # path('adminposting/submit/', views.submit, name='submit'),
    path('home/search/', views.search, name='search'),
    path('search/', views.search, name='search'),
    path('recent/', views.recent, name='search'),
    path('recent/search/', views.recent, name='search'),
    path('contact/contactproble/', views.contactproblem, name='contactprobl'),
    path('blog/', include('blog.urls')),
    path('top_posts/' , include('blog.urs')),
    path('privacy/',views.privacy,name='privacy'),
    path('disclaimer/',views.disclaimer,name='disclimer'),
    path('term/',views.term,name='term'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),    

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
