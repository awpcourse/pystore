from django.contrib import admin
from pystoreapp import models

admin.site.register(models.Order)
admin.site.register(models.OrderedProduct)
admin.site.register(models.Product)
admin.site.register(models.ProductExtras)
admin.site.register(models.UserProfile)


