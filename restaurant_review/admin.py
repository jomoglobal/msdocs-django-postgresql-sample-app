#ORIGINAL FILE:
# from django.contrib import admin

# from .models import Restaurant, Review

# # Register your models here.

# admin.site.register(Restaurant)
# admin.site.register(Review)


#UPDATED FILE:
# restaurant_review/admin.py

from django.contrib import admin
from .models import AzurePricing

admin.site.register(AzurePricing)
