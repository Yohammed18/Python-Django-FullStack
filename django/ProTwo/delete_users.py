import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

# This will allow us to populate 
import django
django.setup()

from AppTwo.models import User

def delete_user():
    User.objects.all().delete()



if __name__ == '__main__':
    print("DELETING ALL USERS")
    delete_user()
    print("DELETION COMPLETED")