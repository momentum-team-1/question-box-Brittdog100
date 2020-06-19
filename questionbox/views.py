from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer

def view_question(request, pk):
	question = get_object_or_404(Question, pk = pk)
	return render(request, "question.html", { "question": question })

@login_required
def post_question(request):
	if request.method == "GET":
		form = QuestionForm()
	else:
		form = QuestionForm(data = request.POST)
		if form.is_valid():
			question = form.save(commit = False)
			question.user = request.user
			question.save()
			return redirect(to = 'view_question', pk = question.pk)
	return render(request, "ask.html", { "form": form })

@login_required
def post_answer(request, question_pk):
	if request.method == 'GET':
		form = AnswerForm()
	else:
		form = AnswerForm(data = request.POST)
		if form.is_valid():
			answer = form.save(commit = False)
			answer.user = request.user
			answer.question = get_object_or_404(Question, pk = question_pk)
			answer.save()
			return redirect(to = 'view_question', pk = question_pk)
	return render(request, "answer.html")

@login_required
def star_answer(request, answer):
	pass # add a star to the answer, then send a success code?

def search(request, query):
	query = request.GET.get('q')
	if query is not None:
		return render(request, "search.html", { "query": query })
	else:
		return render(request, "search.html")

def homepage(request):
	return render(request, "home.html")

def profile(request, username = None):
	if not request.user.is_authenticated():
		pass #403
	if username is None:
		return redirect(to = 'profile', username = request.user.username)
	else:
		pass