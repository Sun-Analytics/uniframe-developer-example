import os
from dotenv import load_dotenv

load_dotenv()

HOST_URL = "https://api.uniframe-dev.com"
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
