from django.db import models

class Reading(models.Model):
    """A check mix energy at a given moment"""
    recorded_at=models.DateTimeField()
    source=models.CharField()
    value_mw=models.FloatField()

    def __str__(self):
        return f"{self.source}@{self.recorded_at}"

