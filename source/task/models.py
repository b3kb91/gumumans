from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    STATUS = [
        ('new', 'Новое'),
        ('in_work', 'В работе'),
        ('completed', 'Завершена')
    ]
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_deleted = models.BooleanField(default=False)

    # soft_delete
    def check_status_to_delete(self):
        if self.status == 'completed':
            self.is_deleted = True
            self.save()

    # change_status
    def change_status(self, new_status):
        pass

    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta:
        db_table = 'task'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['-created_at']
