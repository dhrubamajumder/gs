from django.urls import path
from . import views

urlpatterns = [
    path('co/', views.learn_django)
]
