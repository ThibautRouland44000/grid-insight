import pytest

from energy_data.ingestion import save_generation_mix
from energy_data.models import Reading

FAKE_DATA = {
    "generation_mix_15min_time_scale": [
        {
            "production_type": "NUCLEAR",
            "production_subtype": "TOTAL",
            "values": [
                {
                    "start_date": "2017-06-15T00:00:00+02:00",
                    "end_date": "2017-06-15T00:15:00+02:00",
                    "updated_date": "2017-06-16T00:00:00+02:00",
                    "value": 40000,
                },
                {
                    "start_date": "2017-06-15T00:15:00+02:00",
                    "end_date": "2017-06-15T00:30:00+02:00",
                    "updated_date": "2017-06-16T00:00:00+02:00",
                    "value": 40100,
                },
            ],
        },
        {
            "production_type": "BIOENERGY",
            "production_subtype": "BIOGAS",
            "values": [
                {
                    "start_date": "2017-06-15T00:00:00+02:00",
                    "end_date": "2017-06-15T00:15:00+02:00",
                    "updated_date": "2017-06-16T00:00:00+02:00",
                    "value": 211,
                },
            ],
        },
    ]
}


@pytest.mark.django_db
def test_save_keeps_only_total_subtypes():
    save_generation_mix(FAKE_DATA)
    count = Reading.objects.count()
    assert count == 2
    assert not Reading.objects.filter(source="BIOENERGY").exists()


@pytest.mark.django_db
def test_save_is_idempotent():
    save_generation_mix(FAKE_DATA)
    save_generation_mix(FAKE_DATA)
    count = Reading.objects.count()
    assert count == 2
