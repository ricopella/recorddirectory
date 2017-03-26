from django.db import models

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
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Catalog(models.Model):
    """ Products for Store/Dashboard """
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField()
    status = models.CharField(max_length=200)
    inventory = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    """ Contact Us database """
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    despcrition = models.TextField(max_length=2000)
