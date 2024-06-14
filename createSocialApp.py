import os
import django

# Ensure the project root directory is in the Python path
# Replace '/path/to/your/project' with the actual path to your Django project root
# project_root = '/path/to/your/project'
# if project_root not in sys.path:
    # sys.path.append(project_root)

# Set the environment variable to point to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnwithus.settings')

# Initialize Django
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

# Define your Google OAuth2 credentials
client_id = '1099506374219-2b4i5npc7m23miql7inr9n2ug5n16ek0.apps.googleusercontent.com'
secret = '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'

# Create the Google SocialApp if it doesn't exist
try:
    google_app = SocialApp.objects.get(provider='google')
    print(f"Google SocialApp already exists: {google_app}")
except SocialApp.DoesNotExist:
    site = Site.objects.get_current()
    google_app = SocialApp.objects.create(
        provider='google',
        client_id=client_id,
        secret=secret,
        name='Google'
    )
    google_app.sites.add(site)
    google_app.save()
    print("Google SocialApp created successfully")
