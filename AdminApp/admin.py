from django.contrib import admin
from .models import songDB, admin_registerDB

admin.site.register(songDB)
admin.site.register(admin_registerDB)