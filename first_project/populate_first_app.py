import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


# fake population script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker


fakegen = Faker()
topics