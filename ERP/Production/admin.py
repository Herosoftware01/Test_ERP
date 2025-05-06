from django.contrib import admin
from .models import production

class productionAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')

admin.site.register(production)

# Register your models here.
