from django.contrib import admin
from .models import Quiz, Question, Choice, Text, Radio


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'timeline']
    search_fields = ['title', 'timeline']


admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'quiz', 'title', 'answer_type']
    search_fields = ['quiz', 'title', 'answer_type']


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_option', 'is_correct']
    search_fields = ['is_correct']


admin.site.register(Choice, ChoiceAdmin)


class TextAdmin(admin.ModelAdmin):
    list_display = ['question', 'input_answer', 'correct_answer']
    search_fields = ['question', 'input_answer', 'correct_answer']


admin.site.register(Text, TextAdmin)


class RadioAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_option', 'selected_answer']
    search_fields = ['question', 'answer_option', 'selected_answer']


admin.site.register(Radio, RadioAdmin)

