from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    # fields to be displayed 
    list_display = ('id', 'title', 'is_published', 'suburb', 'price', 'list_date', 'realtor')
    # clickable links
    list_display_links = ('id', 'title')
    # list filter
    list_filter = ('realtor', 'list_date')
    # check and uncheck boxes
    list_editable = ('is_published',)
    # search fields
    search_fields = ('title', 'description', 'address', 'suburb', 'city', 'zipcode', 'price')
    # no. of entries per page
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)
