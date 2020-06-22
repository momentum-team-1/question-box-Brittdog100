from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer, Star

def view_question(request, pk):
	question = get_object_or_404(Question, pk = pk)
	print(pk)
	return render(request, "question.html", { "question": question })

@login_required
def post_question(request):
	if request.method == "GET":
		form = QuestionForm()
	elif request.method == 'POST':
		form = QuestionForm(data = request.POST)
		if form.is_valid():
			question = form.save(commit = False)
			question.user = request.user
			question.save()
			return redirect(to = 'view_question', pk = question.pk)
	else:
		return HttpResponse(status = 405)
	return render(request, "ask.html", { "form": form })

@login_required
def post_answer(request, question_pk):
	question = get_object_or_404(Question, pk = question_pk)
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
	return render(request, "answer.html", { "form": form, "question": question })

@csrf_exempt
@login_required
def star_question(request, pk):
	question = get_object_or_404(Question, pk = pk)
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	if request.method == 'POST':
		star = Star()
		star.user = request.user
		star.question = question
		star.save()
		return HttpResponse(status = 200)
	return HttpResponse(status = 405)

@csrf_exempt
@login_required
def star_answer(request, pk):
	answer = get_object_or_404(Answer, pk = pk)
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	star = Star.objects.filter(answer = pk)
	if request.method == "POST":
		if(len(star) > 0):
			star[0].delete()
		else:
			star = Star()
			star.user = request.user
			star.question = answer.question
			star.answer = answer
			star.save()
		return HttpResponse(status = 200)
	return HttpResponse(status = 405)

@login_required
def is_star_question(request, pk):
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	question = get_object_or_404(Question, pk = pk)
	is_star = (len(request.user.stars.filter(question = question, answer = None)) == 1)
	if query.method == 'GET':
		return JsonResponse({ 'star' : is_star })
	else:
		return HttpResponse(status = 405)

@login_required
def is_star_answer(request, pk):
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	answer = get_object_or_404(Answer, pk = pk)
	is_star = (len(request.user.stars.filter(answer = answer)) == 1)
	if request.method == 'GET':
		return JsonResponse({ 'star': is_star })
	else:
		return HttpResponse(status = 405)

def is_correct(request, pk):
	answer = get_object_or_404(Answer, pk = pk)
	if request.method == 'GET':
		return JsonResponse({ 'correct': answer.is_answer })
	else:
		return HttpResponse(status = 405)

@csrf_exempt
@login_required
def toggle_correct(request, pk):
	answer = get_object_or_404(Answer, pk = pk)
	if (not request.user.is_authenticated) or request.user.username != answer.question.user.username:
		return Httpresponse(status = 403)
	if request.method != 'POST':
		return HttpResponse(status = 405)
	answer.is_answer = not answer.is_answer
	answer.save()
	return HttpResponse(status = 200)

def search(request):
	query = request.GET.get('q')
	if query is not None:
		questions = Question.objects.filter(body__icontains = query)
		answers = Answer.objects.filter(body__icontains = query)
		return render(request, "search.html", { "query": query, "questions": questions, "answers": answers })
	else:
		return render(request, "search.html")

def homepage(request):
	return render(request, "home.html", { "random": get_randoms() })

def profile(request, username = None):
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	if username is None:
		return redirect(to = 'profile', username = request.user.username)
	else:
		return render(request, "profile.html")

def get_randoms():
	return Question.objects.order_by('?').all()[0:5]
