from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Question(models.Model):
    class Meta:
        db_table = "questions"
 
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    question = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.question[0:300]
 
 
class Message(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text[0:300]

 



		
		
		
		
		




