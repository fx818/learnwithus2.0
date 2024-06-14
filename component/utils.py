import random
import string

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))


# email_utils.py

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import BadHeaderError

def sendingmail(subject, message, recipient_list):
    from_email = settings.DEFAULT_FROM_EMAIL
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("mail sent successfully")
    except BadHeaderError:
        return 'Invalid header found.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    return 'Email sent successfully.'





