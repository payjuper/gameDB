# app/services/item_loader.py
import json
import os

# JSON 파일 경로 설정 (VSCode 기준으로 프로젝트 루트에 파일 있을 경우)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ITEM_JSON_PATH = os.path.join(BASE_DIR, "../../equipment_3.json")  # 경로에 따라 조정 가능

with open(ITEM_JSON_PATH, encoding="utf-8") as f:
    item_master = {item["id"]: item for item in json.load(f)}