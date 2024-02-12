from django.contrib import admin

# Register your models here.
# photographers/admin.py

from django.contrib import admin
from .models import Photographer, Portfolio

# Register your models here
admin.site.register(Photographer)
admin.site.register(Portfolio)
