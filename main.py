from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

class GuestbookEntry(BaseModel):
    author: str
    message: str
    timestamp: datetime = datetime.now()

guestbook: List[GuestbookEntry] = []

@app.post("/guestbook")
def add_entry(entry: GuestbookEntry):
    guestbook.append(entry)
    return entry

@app.get("/guestbook")
def get_entries():
    return guestbook
