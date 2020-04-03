from django.contrib import admin

from .models import Listing


# Define what you want to display in the admin table
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')


admin.site.register(Listing, ListingAdmin)
