import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bullet(models.Model):
    class Meta:
        abstract = True
        auto_created = True

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
        NONE = ' '

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    signifier = models.CharField(choices=Signifier.choices, default=Signifier.NONE, max_length=4)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.signifier} {self.symbol} {self.value}"
    