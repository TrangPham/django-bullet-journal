import uuid
from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel

class Bullet(PolymorphicModel):
    @property
    def name(self):
        raise NotImplementedError()
    
    @property    
    def description(self):
        raise NotImplementedError()
    
    @property
    def symbol(self):
        raise NotImplementedError()

    class Signifier(models.TextChoices):
        PRIORITY = '*'
        INSPIRATION = '!'
        NONE = ''

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    signifier = models.CharField(choices=Signifier.choices, default=Signifier.NONE, max_length=4)

    def __str__(self):
        return f"{self.signifier} {self.symbol} {self.value}"
    