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