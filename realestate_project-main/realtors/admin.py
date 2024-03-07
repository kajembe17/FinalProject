from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    # fields to be displayed 
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    # clickable links
    list_display_links = ('id', 'name')
    # search fields
    search_fields = ('name',)
    # no. of entries per page
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin)
