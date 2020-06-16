from django.db import models
from users.models import User

BODY_LENGTH = 32767

class Question(models.Model):
	title = models.TextField(max_length = 255)
	body = models.TextField(max_length = BODY_LENGTH)
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "questions")

class Answer(models.Model):
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "answers")
	#is_answer bool

class Comment(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.SET_NULL, related_name = "comments")
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "comments")
	answer = models.ForeignKey(to = Answer, on_delete = models.CASCADE, related_name = "comments", NULL = True)
	body = models.TextField(max_length = BODY_LENGTH)

class Star(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "stars")
	question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = "stars")
	answer = models.ForeignKey(to = Answer, on_delete = model.CASCADE, related_name = "stars", NULL = True)
