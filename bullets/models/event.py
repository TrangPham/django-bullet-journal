from django.db import models

from bullets.models import Bullet


class Event(Bullet):
    class Meta:
        db_table = "event"

    @property
    def name(self):
        return "Event"

    @property
    def description(self):
        return "noteworth moments in time"

    @property
    def symbol(self):
        return "o"

    datetime = models.DateTimeField()
