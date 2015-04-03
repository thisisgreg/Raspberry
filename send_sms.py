
from twilio.rest import TwilioRestClient
 
account_sid = "AC8db72cd36749487872cfd5fcc0725c37"
auth_token  = "0f46ec208b28c4d06a9a1c7dae4cb080"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Apartment door has been opened",
    to="+16466732481",    # My phone number
    from_="+12018856036") # My Twilio number
print message.sid

