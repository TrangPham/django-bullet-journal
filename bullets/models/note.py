from django.db import models

from bullets.models import Bullet


class Note(Bullet):
    @property
    def name(self):
        return "Note"

    @property
    def description(self):
        return "noteworthy thing"

    @property
    def symbol(self):
        return "-"
