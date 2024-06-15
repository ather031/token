import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sms.settings')

import django
django.setup()

from api.models import Permission

all_permission = [
    {
        'name': 'Create Role', 'code_name': 'role_create', 'module_name': 'Role',
        'description': 'User can create role'
    },
    {
        'name': 'Read Role', 'code_name': 'role_read', 'module_name': 'Role',
        'description': 'User can read role'
    },
    {
        'name': 'Update Role', 'code_name': 'role_update', 'module_name': 'Role',
        'description': 'User can update role'
    },
    {
        'name': 'Delete Role', 'code_name': 'role_delete', 'module_name': 'Role',
        'description': 'User can delete role'
    },
    {
        'name': 'Show Role', 'code_name': 'role_show', 'module_name': 'Role',
        'description': 'User can view role module'
    },
    {
        'name': 'Create User', 'code_name': 'user_create', 'module_name': 'User',
        'description': 'User can create user'
    },
    {
        'name': 'Read User', 'code_name': 'user_read', 'module_name': 'User',
        'description': 'User can read user'
    },
    {
        'name': 'Update User', 'code_name': 'user_update', 'module_name': 'User',
        'description': 'User can update user'
    },
    {
        'name': 'Delete User', 'code_name': 'user_delete', 'module_name': 'User',
        'description': 'User can delete user'
    },
    {
        'name': 'Show User', 'code_name': 'user_show', 'module_name': 'User',
        'description': 'User can view user module'
    },
]


def add_permission():
    for perm_dict in all_permission:
        try:
            Permission.objects.get(code_name=perm_dict['code_name'])
        except Permission.DoesNotExist:
            Permission.objects.create(
                name=perm_dict['name'],
                code_name=perm_dict['code_name'],
                module_name=perm_dict['module_name'],
                description=perm_dict['description'],
            )


if __name__ == '__main__':
    print("Adding permissions")
    add_permission()
