from django.shortcuts import render
from django.http import HttpResponse
import os
from twilio.rest import Client

def send_msg_from_twilio(request):
    account_sid = 'Enter Your Account Sid'
    auth_token = 'Enter Your Token Here'
    try:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Enter Your Text Here",
            from_='Enter Your Phone no Here',
            to='Enter Your Phone no Here'
        )
        print(message.sid)
        return HttpResponse('Message Send Successfully.')
    except Exception as e:
        return HttpResponse('Unable to send message.')


