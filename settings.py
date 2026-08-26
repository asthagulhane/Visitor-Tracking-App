import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables parser
env = environ.Env(
    DEBUG=(bool, False) # Sets a default fallback value
)

# Read the local .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Update core configurations using env reader
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
