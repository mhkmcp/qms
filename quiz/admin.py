from django.contrib import admin
from .models import Quiz, Question, Choice, Text, QuizList


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'time']
    search_fields = ['title', 'time']


admin.site.register(Quiz, QuizAdmin)


class QuizListAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'user', 'is_available']
    search_fields = ['quiz', 'user', 'is_available']


admin.site.register(QuizList, QuizListAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'title', 'answer_type']
    search_fields = ['quiz', 'title', 'answer_type']


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','question', 'text', 'is_correct', 'is_selected']
    search_fields = ['user', 'is_correct']


admin.site.register(Choice, ChoiceAdmin)


class TextAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'input_answer', 'correct_answer']
    search_fields = ['user', 'question', 'input_answer', 'correct_answer']


admin.site.register(Text, TextAdmin)

