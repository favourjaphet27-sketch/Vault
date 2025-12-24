from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import AuditLog
from .serializers import AuditLogSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    serializers = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]

    queryset = AuditLog.objects.all()
