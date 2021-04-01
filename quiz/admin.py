from django.contrib import admin
from .models import Quiz, Question, Choice, Text


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'time']
    search_fields = ['title', 'time']


admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'quiz', 'title', 'answer_type']
    search_fields = ['quiz', 'title', 'answer_type']


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'text', 'is_correct', 'is_selected']
    search_fields = ['is_correct']


admin.site.register(Choice, ChoiceAdmin)


class TextAdmin(admin.ModelAdmin):
    list_display = ['question', 'input_answer', 'correct_answer']
    search_fields = ['question', 'input_answer', 'correct_answer']


admin.site.register(Text, TextAdmin)

