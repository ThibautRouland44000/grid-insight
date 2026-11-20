import pytest
from rest_framework.test import APIClient

from energy_data.models import Reading


@pytest.mark.django_db
def test_readings_list_returns_all_readings():
    Reading.objects.create(
        recorded_at="2017-06-14T22:00:00Z", source="WIND", value_mw=787.0
    )
    Reading.objects.create(
        recorded_at="2017-06-14T22:00:00Z", source="EXCHANGE", value_mw=-2032.0
    )
    client = APIClient()
    response = client.get("/api/readings/")
    body = response.json()
    assert response.status_code == 200
    assert body["count"] == 2
    assert len(body["results"]) == 2
