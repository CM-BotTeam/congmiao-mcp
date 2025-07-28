import json
import aiofiles
import asyncio
from typing import Dict, Any, Optional

async def load_card_json_by_id(card_id: str) -> Optional[Dict[Any, Any]]:
    file_path = "assets/cards.json"
    try:
        async with aiofiles.open(file_path, mode='r', encoding='utf-8') as file:
            content = await file.read()
            data = json.loads(content)
            for item in data:
                # card_id in JSON may be int, so compare as str
                if str(item.get("id")) == str(card_id):
                    return item
            return None
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    
async def load_event_json_by_id(event_id: str) -> Optional[Dict[Any, Any]]:
    file_path = "assets/events.json"
    try:
        async with aiofiles.open(file_path, mode='r', encoding='utf-8') as file:
            content = await file.read()
            data = json.loads(content)
            for item in data:
                # event_id in JSON may be int, so compare as str
                if str(item.get("id")) == str(event_id):
                    return item
            return None
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None