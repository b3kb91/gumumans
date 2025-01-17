from rest_framework import viewsets

from test_work.task.models import Task
from test_work.task.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
