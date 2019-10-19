from django.contrib import admin
#Import all models
from .models import *

# Register your models here.

admin.site.register(category)
admin.site.register(clients)
admin.site.register(products)
admin.site.register(shopping)
admin.site.register(country)
admin.site.register(gender)

