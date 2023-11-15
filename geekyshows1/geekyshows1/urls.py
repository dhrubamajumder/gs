
from django.contrib import admin
from django.urls import path, include
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course.urls')),
    path('py/', views.learn_python),
    path('html/', views.learn_html)
]
