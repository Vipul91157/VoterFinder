import requests
from pathlib import Path


def download_pdf(pdf_url, download_folder="downloads"):

    Path(download_folder).mkdir(exist_ok=True)

    filename = pdf_url.split("/")[-1]

    file_path = Path(download_folder) / filename

    response = requests.get(
        pdf_url,
        timeout=60
    )

    response.raise_for_status()

    with open(file_path, "wb") as pdf:

        pdf.write(response.content)

    return file_path