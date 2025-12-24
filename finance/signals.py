from django.db.models.signals import post_save
from django.dispatch import receiver
from finance.models import Transaction
from rules.services.rule_engine import apply_rules


@receiver(post_save, sender=Transaction)
def run_rules_on_transaction_create(sender, instance, created, **kwargs):
    if created:
        apply_rules(instance)
