from django.contrib import admin
from .models import Rol, Utilizator, Cafenea, Recenzie

@admin.register(Cafenea)
class CafeneaAdmin(admin.ModelAdmin):
    list_display = ('nume', 'adresa', 'latitudine', 'longitudine')
    search_fields = ('nume', 'adresa')

@admin.register(Recenzie)
class RecenzieAdmin(admin.ModelAdmin):
    list_display = ('cafe', 'user', 'rating', 'data_publicarii')
    list_filter = ('rating', 'cafe')

admin.site.register(Rol)
admin.site.register(Utilizator)