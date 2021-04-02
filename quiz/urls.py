from django.urls import path
from .views import index, detail, finish_exam

app_name = 'quiz'

urlpatterns = [
    path('', index, name='home'),
    path('<int:quiz_pk>', detail, name='detail'),
    path('finish', finish_exam, name='finish')
]