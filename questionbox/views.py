from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def view_question(request, pk):
	pass

@login_required
def post_question(request):
	pass

@login_required
def post_answer(request, question_pk):
	pass

@login_required
def star_answer(request, answer):
	pass

def search(request, query):
	pass