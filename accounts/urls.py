from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup', signup_user, name='signup'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
]
