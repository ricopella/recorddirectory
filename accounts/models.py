from django.db import models

# Create your models here.

class Accounts(models.Model):
    """ User Accounts database """
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120) # should it be models.ForeignKey('auth.User')

    def __str__(self):
        return self.username
