import hashlib
import requests
from bs4 import BeautifulSoup

def make_external_id(url: str):
    if not url:
        return None
    return "sha256:" + hashlib.sha256(url.encode()).hexdigest()

def fetch_metadata_from_url(url: str):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string if soup.title else None
        return {"title": title}
    except:
        return {}

def classify_text(text: str):
    text = text.lower()
    if "jazz" in text or "música" in text:
        return {"category": "musica"}
    return {"category": "general"}
