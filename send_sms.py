
from twilio.rest import TwilioRestClient
 
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Apartment door has been opened",
    to=os.environ["PHONE_TO"],    # My phone number
    from_=os.environ["PHONE_FROM"]) # My Twilio number
print message.sid

