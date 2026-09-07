from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

def create_oauth_flow():
    flow_object = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    return flow_object

def authorize():
    flow = create_oauth_flow()
    credentials = flow.run_local_server(port=0)
    with open("token.json", "w") as token_file:
        token_file.write(credentials.to_json())
    return credentials

def load_credentials():
    if not os.path.exists('token.json'):
        cred = authorize()
    else:
        cred = Credentials.from_authorized_user_file('token.json', SCOPES)
        if cred.expired and cred.refresh_token:
            cred.refresh(Request())
            with open("token.json", "w") as token_file:
                token_file.write(cred.to_json())
        elif cred.expired and cred.refresh_token is  None:
            cred = authorize()
    return cred

#authorize()