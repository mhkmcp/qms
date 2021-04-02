from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls', namespace='quiz')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
