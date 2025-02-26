"""
URL configuration for volunteer_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin

def home(request):
    return HttpResponse("<h1>Welcome to the Volunteer Management System</h1>")

urlpatterns = [
    path("", home),  # Homepage
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),  # Replace with actual app name
    path("api/events/", include("events.urls")),  # Replace with actual app name
]
