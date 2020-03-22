from twilio.rest import Client

account_sid = 'ACCOUNT SID'
auth_token = 'AUTH TOKEN'
client = Client(account_sid, auth_token)

i = 0
while i < 10:
    message = client.messages.create(body='Mensaje a Enviar',
                                     from_='whatsapp:+14155238886',
                                     to='whatsapp:+521NumeroCelular')
    i = i + 1

print(message.sid)
