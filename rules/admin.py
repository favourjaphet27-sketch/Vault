from django.contrib import admin
from .models import Rule


# Register your models here.
@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "category", "priority", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
