import logging

from rest_framework import viewsets, permissions, authentication, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer

logger = logging.getLogger(__name__)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(is_deleted=False)
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.TokenAuthentication,)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status != task.STATUS_COMPLETED:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        task.soft_delete()
        logger.info(f"Задача удалена пользователем {self.request.user.username}: {task.title}")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer):
        instance = self.get_object()
        new_status = self.request.data.get('status')

        if new_status:
            try:
                instance.change_status(new_status)
            except ValueError as e:
                raise ValidationError(str(e))

        serializer.save()
        logger.info(
            f"Задача обновлена пользователем {self.request.user.username}: {instance.title}, Новый статус: {new_status}")
