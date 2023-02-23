from django.contrib import admin

from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "published_date")


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
