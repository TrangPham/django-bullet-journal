import uuid
from django.db import models
from polymorphic.models import PolymorphicModel

from bullets.models import Bullet


class List(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.CharField(null=True, blank=True, max_length=255)

    @property
    def items(self):
        return [item.bullet for item in self.list_items.order_by('index')]

class ListItem(models.Model):
    class Meta:
        unique_together = ('list', 'index',)
        indexes = [
            models.Index(fields=('list', 'index',))
        ]
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list_items')
    index = models.PositiveIntegerField()
    bullet = models.ForeignKey(Bullet, on_delete=models.CASCADE)


# TODO: implement nested lists