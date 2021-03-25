from django.contrib import admin
from .models import DSR, Currency, Territory, Resource

# Register your models here.
admin.site.register(DSR)
admin.site.register(Currency)
admin.site.register(Territory)
admin.site.register(Resource)
