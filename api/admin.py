from django.contrib import admin
from api.models import *
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(PartOf)
admin.site.register(Employee)