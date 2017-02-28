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
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Catalog(models.Model):
    """ Products for Store/Dashboard """
    title = models.CharField(max_length=300)
    artist = models.ForeignKey("Artist")
    label = models.ForeignKey("Label")
    genre = models.ForeignKey("Genre")
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField()
    status = models.ForeignKey("Status")
    inventory = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

class Artist(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Label(models.Model):
    label_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    genre_type = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Status(models.Model):
    order_status = models.CharField(max_length=100)
