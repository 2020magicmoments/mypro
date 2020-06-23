from django.urls import path

from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    # path('home/', views.home, name='myblog/home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]