from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Category(models.Model):
    INCOME = "income"
    EXPENSE = "expense"
    CATEGORY_TYPES = [(INCOME, "income"), (EXPENSE, "expense")]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPES)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"


class Transaction(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    TRANSACTION_TYPE = [("debit", "Debit"), ("credit", "Credit")]
    type = models.CharField(max_length=6, choices=TRANSACTION_TYPE)

    def __str__(self):
        return f"{self.type.capitalize()} {self.amount} ({self.account.name})"
