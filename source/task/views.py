from rest_framework import viewsets, permissions, authentication, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(is_deleted=False)
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.TokenAuthentication,)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status != 'completed':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        task.check_status_to_delete()
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
