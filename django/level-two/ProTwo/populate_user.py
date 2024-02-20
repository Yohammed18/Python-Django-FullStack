import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

# This will allow us to populate 
import django
django.setup()

from AppTwo.models import User
from faker import Faker


fakegem = Faker()

def populate(n=5):
    for entry in range(n):

        # create fake name
        fake_name = fakegem.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegem.email()


        # new entry
        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name, email=fake_email)[0]
        


if __name__ == '__main__':
    print("POPULATING DATABSE")
    populate(10)
    print("COMPLETE")
