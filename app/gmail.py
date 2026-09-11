from googleapiclient.discovery import build
from app.oauth import load_credentials
import base64
from bs4 import BeautifulSoup

def get_gmail_profile(credentials):
    service = build( serviceName="gmail", version="v1", credentials=credentials )
    profile = service.users().getProfile(userId="me").execute()
    return profile

def list_messages(credentials, query: str):
    service = build( serviceName="gmail", version="v1", credentials=credentials)
    messages = service.users().messages().list(userId="me", q=query).execute()
    return messages

def get_message(credentials, message_id: str):
    service = build( serviceName="gmail", version="v1", credentials=credentials)
    message = service.users().messages().get(userId="me", id=message_id).execute()
    return message

def decode_part(part):
    data = part.get("body",{}).get("data")

    if data is None:
        return None
    
    text = base64.urlsafe_b64decode(data).decode("utf-8")

    if part.get("mimeType") == "text/plain":
        return text
    elif part.get("mimeType") == "text/html":
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        return text
    else:
        return None

def get_all_parts(part):
    all_parts = [part]
    for child in part.get('parts',[]):
        child_parts = get_all_parts(child)
        all_parts.extend(child_parts)
    return all_parts

def get_message_text(payload):
    parts = get_all_parts(payload)
    text = None
    for part in parts:
        if part.get('mimeType') =='text/plain':
            text = decode_part(part)
            if text is not None:
                break
        elif part.get('mimeType') == 'text/html':
            html_text = decode_part(part)
            if html_text is not None:
                text = html_text
    return text
    
def get_header(payload, header_name:str):
    headers = payload.get('headers',[])

    for header in headers:
        if header.get('name',"").lower() == header_name.lower():
            return header.get('value')
    return None