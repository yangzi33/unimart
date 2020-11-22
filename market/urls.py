from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
	path('', PostListView.as_view(), name='market-home'),
	path('post/<int:pk>/', PostDescriptionView.as_view(), name='post-description'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('about/', views.about, name='market-about'),
]