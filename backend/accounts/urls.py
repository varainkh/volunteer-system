from django.urls import path
from .views import RegisterView, VolunteerProfileDetail, UserDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', VolunteerProfileDetail.as_view(), name='profile'),
    path('user/', UserDetail.as_view(), name='user-detail'),
]
