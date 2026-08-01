from pathlib import Path
import sys

# State Information
STATE_CODE = "S04"
STATE_NAME = "Bihar"

# District Information
DISTRICT_CODE = 35
DISTRICT_NAME = "Siwan"

# Assembly Information
ASSEMBLY_NO = 33

# Detect whether running as a PyInstaller EXE
if getattr(sys, "frozen", False):
    # Folder containing VoterFinder.exe
    BASE_DIR = Path(sys.executable).parent
else:
    # Project folder when running with Python
    BASE_DIR = Path(__file__).resolve().parent

# Folder Paths
DOWNLOAD_FOLDER = BASE_DIR / "downloads"
DATABASE_PATH = BASE_DIR / "data" / "voters.db"

# Base URLs
API_BASE_URL = "https://gateway-voters.eci.gov.in/api/v1/citizen/sir"
PDF_BASE_URL = "https://www.eci.gov.in/eci-backend/public/ER"