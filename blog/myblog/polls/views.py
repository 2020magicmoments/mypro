from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import post
from django.urls import reverse, reverse_lazy
from django.core.files.storage import FileSystemStorage


# Create your views here.

@login_required
def dash(request):
    Post = post.objects.all()
    return render(request, 'dash.html', {'Post': Post})


class PostListView(LoginRequiredMixin, ListView):
    model = post
    template_name = 'post_list.html'
    context_object_name = 'post'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'


class PostUploadView(LoginRequiredMixin, CreateView):
    model = post
    fields = ('title', 'post_data', 'date_posted', 'author', 'post_img')
    success_url = reverse_lazy('post_list')
    template_name = 'post_form.html'

    # context_object_name = 'post'
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class home1(ListView):
    model = post
    template_name = 'home1.html'
    # context_object_name = 'post'
    # ordering = ['-date_posted']
#
# from django.shortcuts import render
# from .forms import UploadFileForm
#
#
# # Imaginary function to handle an uploaded file.
#
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/post/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'post_upload.html', {'form': form})
#
#
# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#
#
# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['title', 'post_data', 'date_posted', 'author', 'post_img']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'upload.html', context)
