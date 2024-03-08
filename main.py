from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("client_id")
client_secret_key = os.getenv("client_secret_key")

print(client_id, client_secret_key)