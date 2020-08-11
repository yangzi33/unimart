from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)


def home(context):
	context = {
			'posts': Post.objects.all(), 
			'title': 'Item Postings',
		}
	return render(request, 'home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


def about(request):
	return render(request, 'about.html', context)