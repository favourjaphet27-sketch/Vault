from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class AuditLog(models.Model):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    ACTIONS = [(CREATE, 'Create'), (UPDATE, 'Update'), (DELETE, 'Delete')]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=6, choices=ACTIONS)
    model_name = models.CharField(max_length=50)
    object_id = models.IntegerField()
    changes = models.JSONField(null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on {self.model_name} ({self.object_id}) by {self.user}"
    


