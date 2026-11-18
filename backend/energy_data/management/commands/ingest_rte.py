from django.core.management.base import BaseCommand

from energy_data.ingestion import save_generation_mix
from energy_data.rte_client import fetch_generation_mix, get_token


class Command(BaseCommand):
    help = "get data from rte api and stock them intop save variable"

    def handle(self, *args, **options):
        token = get_token()
        data = fetch_generation_mix(token)
        count = save_generation_mix(data)
        self.stdout.write(self.style.SUCCESS(f"{count} data saved"))
