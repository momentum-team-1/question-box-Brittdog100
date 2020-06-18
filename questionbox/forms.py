from django import forms
from users.models import User
from .models import Question, Answer, Comment, Star

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		user = User
		fields = [
			'title',
			'body'
		]