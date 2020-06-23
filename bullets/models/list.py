import uuid
from django.db import models
from polymorphic.models import PolymorphicModel

from bullets.models import Bullet


class List(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.CharField(null=True, blank=True, max_length=255)

    def view(self):
        return "\n".join([item.view() for item in self.list_items.all()])

    def __str__(self):
        return f"{self.name} ({self.uuid})"

class ListItem(PolymorphicModel):
    class Meta:
        unique_together = ('list', 'index',)
        indexes = [
            models.Index(fields=('list', 'index',))
        ]
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list_items')
    index = models.PositiveIntegerField()

class BulletListItem(ListItem):
    content = models.ForeignKey(Bullet, on_delete=models.CASCADE)

    def view(self):
        return self.content.view()

class NestedListItem(ListItem):
    content = models.ForeignKey(List, on_delete=models.CASCADE)

    def view(self):
        return "\n".join(["\t" + item for item in self.content.view().split("\n")])
