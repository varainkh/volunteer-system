from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TaskViewSet, ParticipationViewSet, VolunteerPerformance

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'participations', ParticipationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('performance/', VolunteerPerformance.as_view(), name='performance'),
]
