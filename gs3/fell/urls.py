from django.urls import path
from . import views
urlpatterns = [
    path('fel/', views.learn_fell)
]
