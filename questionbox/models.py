from django.db import models
from users.models import User

BODY_LENGTH = 32767

class Question(models.Model):
	title = models.TextField(max_length = 255)
	body = models.TextField(max_length = BODY_LENGTH)
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "questions", null = True)
	timestamp = models.DateTimeField()

class Answer(models.Model):
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "answers")
	is_answer = models.BooleanField(default = False)
	timestamp = models.DateTimeField()

class Comment(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "comments", null = True)
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "comments")
	answer = models.ForeignKey(to = Answer, on_delete = models.CASCADE, related_name = "comments", null = True)
	body = models.TextField(max_length = BODY_LENGTH)
	timestamp = models.DateTimeField()

class Star(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "stars")
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "stars")
	answer = models.ForeignKey(to = Answer, on_delete = models.CASCADE, related_name = "stars", null = True)
