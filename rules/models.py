from django.db import models
from django.conf import settings
from finance.models import Category, Transaction

User = settings.AUTH_USER_MODEL
class Rule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rules')
    name = models.CharField(max_length=255)
    conditions = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='rules')
    priority = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}(Priority{self.priority})"
    

class RuleExecution(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name="executions")
    transactions = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="executions")
    executed_at = models.DateTimeField(auto_now_add=True)