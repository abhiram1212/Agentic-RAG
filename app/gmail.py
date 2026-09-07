from googleapiclient.discovery import build

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

