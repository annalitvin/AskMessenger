from django.contrib import admin

from .models import Question, Message

admin.site.register(Question)
admin.site.register(Message)
