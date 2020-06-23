from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from polls.models import post


class home(ListView):
    model = post
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
