# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New User Registration'
        message = f'User {instance.username} has registered on your website LearnWithUs.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['techgeekanurag818@gmail.com']  # Change to your email

        send_mail(subject, message, from_email, recipient_list)
