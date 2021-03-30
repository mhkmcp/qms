from django.contrib import admin
from .models import Quiz, Question, Option, Text, Radio


# @admin.register(Quiz)
# class QuizAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug']
#     prepopulated_fields = {'slug': ('title')}


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Text)
admin.site.register(Radio)

