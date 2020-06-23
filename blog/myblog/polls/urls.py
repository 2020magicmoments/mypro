from django.conf import settings
from django.template.context_processors import static
from django.urls import path, include
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from . import views
from .views import (PostUploadView, PostDeleteView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', views.dash, name='dash'),
    path('home1', views.home1.as_view(), name='home1'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('single_post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('delete_post/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('upload/', PostUploadView.as_view(), name='post_upload'),
    # path('upload_file/', views.upload_file, name='upload_file'),
    # path('post/', views.upload_apost.s_view(), name='PostListView'),

]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)