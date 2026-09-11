for part in message["payload"].get("parts", []):
#     if part.get("mimeType") == "text/html":
#         print(part["body"].keys())
#         print(part["body"].get("size"))
#         text = base64.urlsafe_b64decode(part["body"].get("data")).decode("utf-8")
#         soup = BeautifulSoup(text, "html.parser")
#         text = soup.get_text(separator="\n", strip=True)
#         print(text[:500])