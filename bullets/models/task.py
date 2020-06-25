from django.db import models

from bullets.models import Bullet

class Task(Bullet):
    class Meta:
        db_table = "task"

    @property
    def name(self):
        return "Task"

    @property
    def description(self):
        return "a thing to do"

    @property
    def symbol(self):
        return self.status

    class Status(models.TextChoices):
        INCOMPLETE = '.'
        COMPLETE = 'x'

    status = models.CharField(choices=Status.choices, default=Status.INCOMPLETE, max_length=4)
