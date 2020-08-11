from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	# TODO: add ImageField that allows multiple 
	# images upload 
	short_description = models.TextField(max_length=100)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	# requires modifications 
	location = models.CharField(max_length=100)
	# price = models.

	def __str__(self):
		return self.title 

	# TODO: get_absolute_url
