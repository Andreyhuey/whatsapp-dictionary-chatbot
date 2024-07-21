from twilio.rest import Client

account_sid = '<account_sid>'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+2348064525018',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+234705550113'
)

print(message.sid)