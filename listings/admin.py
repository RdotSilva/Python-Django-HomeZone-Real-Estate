from django.contrib import admin

from .models import Listing


# Define what you want to display in the admin table
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')

    # Choose what items can be clicked as a link to navigate to listing
    list_display_links = ('id', 'title')

    # Filter items
    list_filter = ('realtor',)

    # Clickable published/unpublished
    list_editable = ('is_published',)

    # Adds a search bar, these fields will be searchable
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')

    # Pagination, number of listings per page
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
