from django.db import models
from django.utils import timezone

# Create your models here.
class Gallery(models.Model):
	gallery_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='gallery_pics/', default='media/default.jpeg')
	slug = models.SlugField(max_length=200, default='gallery_name', unique=True)
	date_created = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['gallery_name']

	# Creating a donder str method;
	def __str__(self):
		return self.gallery_name


class Post(models.Model):
	choices = (
			('events', 'events'),
			('news', 'news')
		) 
	title = models.CharField(max_length=50, blank=True)
	image = models.ImageField(upload_to='events/', default='media/default.jpeg')
	category = models.CharField(max_length=20, choices=choices, default='news')
	description = models.CharField(max_length=300, blank=True, default='more info here')
	date_created = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.event_name

