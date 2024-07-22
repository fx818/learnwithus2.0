from django.contrib import admin

# Register your models here.
from . import models

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'question','college')
    list_filter = ('email',)
    search_fields = ('name', 'email')

admin.site.register(models.ContactModel, ContactModelAdmin)