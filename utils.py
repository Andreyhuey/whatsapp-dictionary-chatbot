from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.getenv('TWILIO_NUMBER')
to_number = os.getenv('TO_NUMBER')

message = client.messages.create(
  from_=f'whatsapp:{twilio_number}',  
  body='Your appointment is coming up on July 21 at 3PM',
  to=f'whatsapp:{to_number}'
)

print(message.sid)