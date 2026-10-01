from django.db import models


class Reading(models.Model):
    """A check mix energy at a given moment"""

    SOURCE_CHOICES=[
        ("NUCLEAR", "Nucléaire"),
        ("WIND", "Éolien"),
        ("BIOENERGY", "Bioénergie"),
        ("FOSSIL_GAS", "Gaz fossile"),
        ("FOSSIL_OIL", "Fioul"),
        ("FOSSIL_HARD_COAL", "Charbon"),
        ("HYDRO", "Hydraulique"),
        ("SOLAR", "Solaire"),
        ("EXCHANGE", "Échange"),
        ("PUMPING", "Pompage"),
    ]

    recorded_at=models.DateTimeField()
    source=models.CharField(max_length=20, choices=SOURCE_CHOICES)
    value_mw=models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["recorded_at","source"], name="unique_reading_per_time_and_source")
        ]

    def __str__(self):
        return f"{self.source}@{self.recorded_at}"


