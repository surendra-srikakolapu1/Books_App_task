
from django.contrib import admin
from django.urls import path, include
from Email_App import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Email_App.urls')),
]
