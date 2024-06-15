from django.db import models

class Employee(models.Model):
    full_name               = models.CharField(max_length=90, blank=True, null=True)
    address                 = models.TextField(blank=True, null=True)
    email                   = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return str(self.full_name) + ' | ' + str(self.email)