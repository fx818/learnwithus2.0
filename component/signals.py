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










from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from .models import CustomUser

@receiver(user_signed_up)
def social_account_update(sender, request, user, **kwargs):
    social_account = SocialAccount.objects.get(user=user)
    data = social_account.extra_data

    # Update the CustomUser fields
    custom_user = CustomUser.objects.get(id=user.id)
    custom_user.email = data.get('email', user.email)
    custom_user.first_name = data.get('given_name', user.first_name)
    custom_user.last_name = data.get('family_name', user.last_name)
    custom_user.profile_pic = data.get('picture', user.profile_pic)
    custom_user.save()




# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount

CustomUser = get_user_model()

@receiver(post_save, sender=CustomUser)
def sync_custom_user(sender, instance, created, **kwargs):
    if created:
        # Get the social account data if it exists
        try:
            social_account = SocialAccount.objects.get(user=instance)
            data = social_account.extra_data
            instance.email = data.get('email', instance.email)
            instance.first_name = data.get('given_name', instance.first_name)
            instance.last_name = data.get('family_name', instance.last_name)
            instance.profile_pic = data.get('picture', instance.profile_pic)
            print(instance)
            print(instance.profile_pic)
            instance.save()
            print("user added")
        except SocialAccount.DoesNotExist:
            print("didn't added back")
            pass


