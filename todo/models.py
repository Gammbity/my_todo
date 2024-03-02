from django.contrib.auth import get_user_model

User = get_user_model()
from django.db import models


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=255)
    is_did = models.BooleanField(default=False)
    when = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.todo
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'