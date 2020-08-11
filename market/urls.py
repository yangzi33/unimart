from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='market-home'),
	path('about/', views.about, name='market-about'),
]
