import os
from datetime import datetime

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# from main_app.models import Bird, Animal
#
# b = Bird.objects.create(wing_span=10, name='sada', species='dasda', birth_date=datetime.now(), sound='das')

# Create queries within functions
