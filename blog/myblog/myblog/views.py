from . import urls
from django.views.generic import ListView
from polls.models import post

class home(ListView):
    model = post
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
