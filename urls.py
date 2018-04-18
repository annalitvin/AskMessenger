from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.index, name='questions'),
	path('register/', views.RegisterFormView.as_view()),
	path('login/', views.LoginFormView.as_view()),
	path('logout/', views.LogoutView.as_view()),
	path('addquestion/', views.form_question, name='addquestion'),
	path('question/<int:id>', views.question_page, name='question'),
	path('updatequestions', views.updatequestions, name='updatequestions'),
    path('updatecomments/<int:id>', views.update_comments, name='updatecomments'),
	path('addcomment/<int:id>', views.add_comment, name='addcomment'),

]