import requests
from django.conf import settings

TOKEN_URL = "https://digital.iservices.rte-france.com/token/oauth/"

GENERATION_URL = "https://digital.iservices.rte-france.com/open_api/actual_generation/v1/sandbox/generation_mix_15min_time_scale"


def get_token():

    identifiant = settings.CONNECTION_API['RTE_CLIENT_ID']
    secret = settings.CONNECTION_API['RTE_CLIENT_SECRET']
    response = requests.post(TOKEN_URL, auth=(identifiant, secret), headers={"Content-Type":"application/x-www-form-urlencoded"}, timeout=10)
    response.raise_for_status()
    response = response.json()
    access_token = response["access_token"]

    return access_token

def fetch_generation_mix(access_token):

    response = requests.get(GENERATION_URL, headers={"Authorization":f"Bearer {access_token}"}, params={"production_subtype":"TOTAL"}, timeout=10)
    response.raise_for_status()
    response=response.json()

    return response 