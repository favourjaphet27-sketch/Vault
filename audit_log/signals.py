from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from finance.models import Account, Category, Transaction
from .models import AuditLog

MODELS = [Account, Category, Transaction]


@receiver(post_save)
def create_audit_log(sender, instance, created, **kwargs):
    if sender in MODELS:
        action = "CREATE" if created else "UPDATE"
        AuditLog.objects.create(
            user=instance.user,
            action=action,
            model_name=sender.__name__,
            object_id=instance.id,
            changes=None,
        )


@receiver(post_delete)
def delete_audit_log(sender, instance, **kwargs):
    if sender in MODELS:
        AuditLog.objects.create(
            user=instance.user,
            action="DELETE",
            model_name=sender.__name__,
            object_id=instance.id,
            changes=None,
        )
