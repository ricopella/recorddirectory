from django.db import models

# Create your models here.

class Accounts(models.Model):
    """ User Accounts database """
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120) # should it be models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    street_address1 = models.CharField(max_length=120, null=True)
    street_address2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, null=True)
    state = models.CharField(max_length=3, null=True)
    country = models.CharField(max_length=120, default="USA", null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
