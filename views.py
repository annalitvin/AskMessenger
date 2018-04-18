from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
	
import json
from datetime import datetime


def index(request):
    questions = Question.objects.all().order_by("pub_date").reverse()
	
    return render(request, "questions_list.html", {"questions": questions})
	

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login		
		
class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)		
		
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


		
from django import forms
 
from .models import Question, Message
 
 
class QuestionForm(forms.Form): 
    question_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )

from django.views import View
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf

@login_required
def form_question(request):
    if request.POST:
        form = request.POST
        question = Question()
        question.author = auth.get_user(request)
        question.question = form['message']
        question.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, 'addquestion.html')


def question_page(request, id):
    if request.POST:
        form = request.POST
        message = Message()
        message.author = auth.get_user(request)
        message.question = Question.objects.get(pk = id)
        message.text = form['message']
        message.save()
	
    q = Question.objects.get(pk = id)
    comments = Message.objects.all().filter(question = q).order_by("date").reverse()

    return render(request, "question.html", {"question": q, "comments": comments})


@login_required
def add_comment(request, id):
    if request.POST:
        form = request.POST
        message = Message()
        message.author = auth.get_user(request)
        message.question = Question.objects.get(pk = id)
        message.text = form['message']
        message.save()
    return update_comments (request, id)


def update_comments (request, id):
    q = Question.objects.get(pk = id)
    data = {'comments': []}
    comments = Message.objects.all().filter(question = q).order_by("date").reverse()
    for comment in comments:
        data['comments'].append({'id': str(comment.id), 'author': str(comment.author), 'question': str(comment.question),
                     'date': datetime.strftime(comment.date, "%Y.%m.%d %H:%M:%S"), 'text': str(comment.text)})
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')


def updatequestions(request):
    questions = Question.objects.all().order_by("pub_date").reverse()
    data = {'questions': []}
    for question in questions:
        data['questions'].append({'id': str(question.id), 'author': str(question.author), 'question': str(question.question),
                     'pub_date': datetime.strftime(question.pub_date, "%Y.%m.%d %H:%M:%S")})
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
 



