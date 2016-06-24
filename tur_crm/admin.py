from django.contrib import admin
from tur_crm.models import *
# Register your models here.


class EmailInline(admin.TabularInline):
    model = ClientEmail

class PhoneInline(admin.TabularInline):
    model = ClientPhone

class ClientAdmin(admin.ModelAdmin):
    inlines = [EmailInline, PhoneInline]

admin.site.register(Client, ClientAdmin)
admin.site.register(Tour)
admin.site.register(Payment)
