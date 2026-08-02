import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------
# Application
# ---------------------------------
APP_NAME = "Gyanibaba"
APP_ICON = "🤖"

# ---------------------------------
# Gemini
# ---------------------------------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-3.6-flash"

# ---------------------------------
# Database
# ---------------------------------
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# ---------------------------------
# Uploads
# ---------------------------------
UPLOAD_FOLDER = "uploads"