from django.db import models

from bullets.models import Bullet


class Note(Bullet):
    class Meta:
        db_table = "note"

    @property
    def name(self):
        return "Note"

    @property
    def description(self):
        return "noteworthy thing"

    @property
    def symbol(self):
        return "-"
