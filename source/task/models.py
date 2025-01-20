from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_NEW, 'Новое'),
        (STATUS_IN_PROGRESS, 'В работе'),
        (STATUS_COMPLETED, 'Завершено')
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, max_length=15, default='new')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # soft_delete
    def check_status_to_delete(self):
        if self.status == 'completed':
            self.is_deleted = True
            self.save()

    # change_status
    def change_status(self, new_status):
        allowed_transitions = {
            self.STATUS_NEW: [self.STATUS_IN_PROGRESS],
            self.STATUS_IN_PROGRESS: [self.STATUS_COMPLETED],
            self.STATUS_COMPLETED: []
        }
        if new_status not in allowed_transitions[self.status]:
            raise ValueError(f"Нельзя сменить статус с '{self.get_status_display()}' на '{dict(self.STATUS_CHOICES).get(new_status)}'")
        self.status = new_status
        self.save()


    class Meta:
        db_table = 'task'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['-created_at']