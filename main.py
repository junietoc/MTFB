from twilio.rest import Client
import keys
import bracelets

client = Client(keys.account_sid, keys.auth_token)
bracelet = bracelets.random_bracelet()

target_number = input("Please write your phone number: ")
message = client.messages.create(    
    body = f"Your random bracelet initials are: {bracelet}",
    from_=keys.twilio_number,
    to=f"+{target_number}",
)