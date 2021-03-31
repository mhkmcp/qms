from django.contrib import admin
from .models import Quiz, Question, Choice, Text, Radio


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'timeline']
    search_fields = ['title', 'timeline']


admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'title', 'answer_type']
    search_fields = ['quiz', 'title', 'answer_type']


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['answer', 'is_correct']
    search_fields = ['is_correct']


admin.site.register(Choice, ChoiceAdmin)


admin.site.register(Text)
admin.site.register(Radio)

