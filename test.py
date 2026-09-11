from app.oauth import load_credentials
from app.gmail import get_gmail_profile
from app.gmail import list_messages
import app.gmail as gmail
import base64
from bs4 import BeautifulSoup

credentials = load_credentials()
profile = get_gmail_profile(credentials)
result = list_messages(credentials, query="from:adobe newer_than:7d")
print(result)
message = gmail.get_message(credentials, message_id=result.get("messages")[0]["id"])
# print(message["payload"].get("parts"))
# print(message["payload"].get("parts", []))
# print(result.keys())
# print(result.get("resultSizeEstimate"))
# print(result.get("messages")[:3])
# print(message.keys())
# for part in message["payload"].get("parts", []):
#     if part.get("mimeType") == "text/html":
#         print(part["body"].keys())
#         print(part["body"].get("size"))
#         text = base64.urlsafe_b64decode(part["body"].get("data")).decode("utf-8")
#         soup = BeautifulSoup(text, "html.parser")
#         text = soup.get_text(separator="\n", strip=True)
#         print(text[:500])
# for part in message["payload"].get("parts"):
#     print(gmail.decode_part(part))

# parts = gmail.get_all_parts(message['payload'])

# for part in parts:
#     print(part.get('mimeType'))

# print(gmail.get_message_text(message['payload']))

payload = message["payload"]

print(gmail.get_header(payload, "Subject"))
print(gmail.get_header(payload, "From"))
print(gmail.get_header(payload, "Date"))