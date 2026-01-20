import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobackend.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password')
    print("Superuser created")

# Create regular user
if not User.objects.filter(username='user').exists():
    User.objects.create_user('user', 'user@example.com', 'password123')
    print("User created")
