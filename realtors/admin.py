from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    # Define what you want to display in the admin table
    list_display = ('id', 'name', 'email', 'hire_date')

    # Choose what items can be clicked as a link to navigate to listing
    list_display_links = ('id', 'name')

    # Adds a search bar, these fields will be searchable
    search_fields = ('name',)

    # Pagination
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
