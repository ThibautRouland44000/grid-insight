from datetime import datetime

from .models import Reading


def save_generation_mix(data):
    items = data["generation_mix_15min_time_scale"]
    compteur = 0

    for item in items:
        if item["production_subtype"] != "TOTAL":
            continue

        for mesure in item["values"]:
            date = datetime.fromisoformat(mesure["start_date"])
            if mesure["value"] is None:
                continue
            Reading.objects.update_or_create(
                recorded_at=date,
                source=item["production_type"],
                defaults={"value_mw": mesure["value"]},
            )
            compteur += 1

    return compteur
