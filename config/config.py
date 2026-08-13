from pathlib import Path
#this path takes to the parent folder (no. of .parent means number of upper folder hop)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#path of folder in which I have store json
JSON_FOLDER = PROJECT_ROOT / "json"

#path of admindatabase.json file
ADMIN_DATABASE = JSON_FOLDER / "admindatabase.json"

#path of customerdatabase.json file
CUSTOMER_DATABASE = JSON_FOLDER / "customerdatabase.json"

#path of bus database
BUSDATABASE = JSON_FOLDER / "busdatabase.json"