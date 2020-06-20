from django.db import models
from users.models import User

# The maximum length of text bodies.
BODY_LENGTH = 65535

class Question(models.Model):
	title = models.TextField(max_length = 255)
	body = models.TextField(max_length = BODY_LENGTH)
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "questions", null = True)
	timestamp = models.DateTimeField(auto_now_add = True)

class Answer(models.Model):
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "answers")
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "answers", null = True)
	body = models.TextField(max_length = BODY_LENGTH)
	is_answer = models.BooleanField(default = False)
	timestamp = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "comments", null = True)
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "comments")
	answer = models.ForeignKey(to = Answer, on_delete = models.CASCADE, related_name = "comments", null = True)
	body = models.TextField(max_length = BODY_LENGTH)
	timestamp = models.DateTimeField(auto_now_add = True)

class Star(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "stars")
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "stars")
	answer = models.ForeignKey(to = Answer, on_delete = models.CASCADE, related_name = "stars", null = True)
