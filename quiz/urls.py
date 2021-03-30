from django.urls import path
from .views import index, detail

app_name = 'quiz'

urlpatterns = [
    path('', index, name='home'),
    path('detail', detail, name='detail'),
]