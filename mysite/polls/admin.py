from django.contrib import admin

# Register your models here.

from .models import Question, Choice, User, Test, Filters

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Test)
admin.site.register(Filters)
