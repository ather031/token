from django.db import models

class PartOf(models.Model):
    user            = models.OneToOneField('User', on_delete=models.CASCADE)
    role            = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' | ' + str(self.role)