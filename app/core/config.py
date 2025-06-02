# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in .env file")
