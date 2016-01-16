from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class UserProfile(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    birthdate = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    # status = models.IntegerField()
    # account_type = models.IntegerField()
    # hash_user = models.CharField(max_length=255)
    # last_reset_request = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(User)

    def __unicode__(self):
        return u'{} {}'.format(self.user.first_name, self.user.last_name)


class Order(models.Model):
    STATUSES = (
        (0, 'Pending'),
        (1, 'Confirmed'),
        (2, 'Cancelled')
    )

    user = models.ForeignKey(UserProfile, related_name='products')
    status = models.IntegerField(choices=STATUSES)
    total = models.FloatField()
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'{}'.format(self.id)


class Product(models.Model):

    STATUSES = (
        (0, 'Out of stock'),
        (1, 'Available'),
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUSES)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'{}'.format(self.id)


class OrderedProduct(models.Model):

    order = models.ForeignKey(Order, related_name='ordered_products')
    product = models.OneToOneField(Product)
    quantity = models.IntegerField()

    def __unicode__(self):
        return u'{}'.format(self.id)


class ProductExtras(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField()
    created = models.DateTimeField(auto_now=True)

    products = models.ManyToManyField(Product)
    ordered_products = models.ManyToManyField(OrderedProduct)

    class Meta:
        ordering = ['-name']

    def __unicode__(self):
        return u'{}'.format(self.name)
