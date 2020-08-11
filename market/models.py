from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	# TODO: add ImageField that allows multiple 
	# images upload 
	description = models.TextField()
	date_listed = models.DateTimeField(default=timezone.now)
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	# requires modifications 
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.title 

	# TODO: get_absolute_url
