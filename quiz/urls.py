from django.urls import path
from .views import index, detail, test, submit

app_name = 'quiz'

urlpatterns = [
    path('', index, name='home'),
    path('<int:quiz_pk>', detail, name='detail'),
    path('test/<int:quiz_pk>', test, name='test'),
    path('submit', submit, name='submit'),
]