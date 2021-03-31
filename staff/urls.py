from django.urls import path
from .views import index, detail, radio_view

app_name = 'staff'

urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:quiz_pk>', detail, name='detail'),
    # path('detail/<int:quiz_pk>/radio', radio_view, name='radio-form-view'),
]