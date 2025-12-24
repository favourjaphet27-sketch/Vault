from rest_framework import serializers
from .models import Rule, RuleExecution


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = "Rule"
        fields = "__all__"
        read_only_fields = ("user",)


