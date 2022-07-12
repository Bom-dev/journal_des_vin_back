from django.contrib import admin
from journal_des_vin.models import Wine, Winemaker

# Register your models here.

admin.site.register(Winemaker)
admin.site.register(Wine)