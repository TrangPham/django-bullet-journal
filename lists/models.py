import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from bullets.models import Bullet

class List(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.CharField(null=True, blank=True, max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.uuid})"


class ListItem(models.Model):
    class Meta:
        unique_together = ('list', 'index',)
        indexes = [
            models.Index(fields=('list', 'index',))
        ]
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ["index"]
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    index = models.PositiveIntegerField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_uuid = models.UUIDField()
    content = GenericForeignKey('content_type', 'content_uuid')