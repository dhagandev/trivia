from django.shortcuts import render, redirect
import requests
import random

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Question, User

# Create your views here.
def home(request):
	return render(request, 'main_app/home.html')

def signup(request):
	error_message = ''
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
		return redirect('/')
	else:
		error_message = 'Invalid sign up - try again'
		form = UserCreationForm()
		context = {'form': form, 'error_message': error_message}
	return render(request, 'registration/signup.html', context)

def user_profile(request, user_id):
	user = User.objects.get(id=user_id)
	profile = Profile.objects.get(user=user)
	return render(request, 'main_app/profile.html', {
		'profile': profile,
	})

def user_ranking(request):
	all_profiles = Profile.objects.all()
	for profile in all_profiles: 
		if (profile.q_answered != 0):
			profile.percent = profile.q_correct / profile.q_answered
		else:
			profile.percent = 0
	return render(request, 'main_app/user_ranking.html', {
		'all_profiles': all_profiles
	})

def question(request):
	questions = Question.objects.all()
	response = requests.get('https://opentdb.com/api.php?amount=1')
	trivia_data = response.json()
	if (not questions.filter(q_text=trivia_data['results'][0]['question']).exists()):
		new_q = Question(
			category=trivia_data['results'][0]['category'],
			difficulty=trivia_data['results'][0]['difficulty'],
			q_text=trivia_data['results'][0]['question'],
			correct_ans=trivia_data['results'][0]['correct_answer'],
			incorrect_ans=trivia_data['results'][0]['incorrect_answers']
		)
		new_q.save()
	# Get question id from db based on question
	q_id = questions.filter(q_text=trivia_data['results'][0]['question'])[0].id
	return redirect('question_display', question_id=q_id)

def question_display(request, question_id):
	question = Question.objects.get(id=question_id)
	answers = question.incorrect_ans
	answers.append(question.correct_ans)
	random.shuffle(answers)
	return render(request, 'main_app/question_display.html', {
		'question': question,
		'answers': answers
	})

def answer(request, question_id, player_choice):
	question = Question.objects.get(id=question_id)
	correct = question.correct_ans
	profile = Profile.objects.get(user=request.user)
	if (correct == player_choice):
		profile.q_correct += 1
	profile.q_answered += 1
	print(profile.q_answered)
	print(profile.q_correct)
	profile.save()
	return render(request, 'main_app/answer.html', {
		'question': question,
		'player_choice': player_choice
	})