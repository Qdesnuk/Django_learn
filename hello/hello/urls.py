"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/', views.details, name='details'),
    # re_path(r'^products/$', views.products),
    # re_path(r'^products/(?P<product_id>\d+)/', views.products, name='products'),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users, name='users'),
    path('products/<int:product_id>/', views.products, name='products'),
    path('users/', views.users),
    path('admin/', admin.site.urls),
]
