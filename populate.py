import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sms.settings')
import django
django.setup()

from api.models import User, Role, Permission, PartOf

def populate():
    permissions = Permission.objects.all()
    try:
        role = Role.objects.get(code_name='su')
    except Role.DoesNotExist:
        role = Role.objects.create(name='SuperUser', code_name='su')

    role.permissions.clear()
    role.permissions.add(*permissions)
    role.save()

    try:
        user = User.objects.get(username='superuser')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            username="superuser",
            password="superuser123",
            first_name="super",
            last_name="user",     
        )
    user.save()
    

    try:
        part_of = PartOf.objects.create(user=user, role=role)
        part_of.save()
    except:
        pass

if __name__ == '__main__':
    print("Starting PSIMS population script...")
    populate()
