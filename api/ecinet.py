"""
ECINET API Functions
"""

import requests

from config import API_BASE_URL
from api.headers import HEADERS


def get_assemblies(district_number):
    """
    Get all assemblies of a district.
    """

    url = f"{API_BASE_URL}/getAsmblyByDist?District={district_number}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.json()
def get_polling_stations(assembly_number):
    """
    Get all polling stations (parts) of an assembly.
    """

    url = f"{API_BASE_URL}/getPartByAc?Asmbly={assembly_number}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.json()
