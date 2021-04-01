from django.urls import path
from .views import *

app_name = 'staff'

urlpatterns = [
    path('', index, name='home'),
    path('<int:quiz_pk>', detail, name='detail'),
    path('radio', radio_view, name='radio'),
    path('text', text_view, name='text'),
    path('choice', choice, name='choice'),

    # path('edit')
]