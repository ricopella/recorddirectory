from django.db import models

# Create your models here.

class Accounts(models.Model):
    """ User Accounts database """
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120) # should it be models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    street_address1 = models.CharField(max_length=120)
    street_address2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=3)
    country = models.CharField(max_length=120)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.username
