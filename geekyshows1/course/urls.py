
from django.urls import path
from .views import *
from course import views

urlpatterns = [
    path('', learn_django, name='learn-django'),
    # path('python/', views.learn_python)
]