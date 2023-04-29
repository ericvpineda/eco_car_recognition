from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.register(Car, CarAdmin)