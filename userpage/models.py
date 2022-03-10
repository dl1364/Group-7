import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
	user_name = models.CharField(max_length=50)
	start_date = models.DateTimeField('date published')
	def __str__(self):
		return self.user_name
	def was_published_recently(self):
		return self.start_dat >= timezone.now() - datetime.timedelta(days=1)

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	poster_id = models.IntegerField(default=1)
	post_text = models.CharField(max_length=256)
	like_num = models.IntegerField(default=0)
	comment_num = models.IntegerField(default=0)
	def __str__(self):
		return self.post_text

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=256)
	like_num = models.IntegerField(default=0)
	def __str__(self):
		return self.comment_text