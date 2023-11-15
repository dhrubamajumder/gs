
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('co/', include('course.urls')),
    path('fe/', include('fees.urls')),
    path('fel/', include('fell.urls')),
]
