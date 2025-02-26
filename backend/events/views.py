from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Task, Participation
from .serializers import EventSerializer, TaskSerializer, ParticipationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAdminUser]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAdminUser]

class VolunteerPerformance(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        participations = request.user.participations.all()
        total_hours = sum([p.hours_contributed for p in participations])
        events = [{'title': p.event.title, 'hours': p.hours_contributed} for p in participations]
        data = {
            'total_hours': total_hours,
            'events': events,
        }
        return Response(data)
