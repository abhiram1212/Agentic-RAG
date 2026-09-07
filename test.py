from app.oauth import load_credentials
from app.gmail import get_gmail_profile
from app.gmail import list_messages
import app.gmail as gmail

credentials = load_credentials()
profile = get_gmail_profile(credentials)
result = list_messages(credentials, query="from:amazon newer_than:7d")
message = gmail.get_message(credentials, message_id=result.get("messages")[0]["id"])

# print(result.keys())
# print(result.get("resultSizeEstimate"))
# print(result.get("messages")[:3])
# print(message.keys())
for part in message["payload"].get("parts", []):
    if part.get("mimeType") == "text/html":
        print(part["body"].keys())

print(part["body"].get("size"))
print(part["body"].get("data") is not None)