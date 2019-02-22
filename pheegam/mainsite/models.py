from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return self.user.username

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Project(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(max_length=500)
	link = models.CharField(max_length=50)
	image = models.ImageField(default='default.jpg', upload_to='project_pics')
	image2 = models.ImageField(default='default.jpg', upload_to='project_pics')
	image3 = models.ImageField(default='default.jpg', upload_to='project_pics')

	def __str__(self):
		return self.title

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	image = models.ImageField(default='default.jpeg', upload_to='book_covers')
	current = models.BooleanField(default=False)
	def __str__(self):
		return self.title

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
