from django.urls import path
from . import views

urlpatterns = [
    path('fe/', views.learn_fees)
]
