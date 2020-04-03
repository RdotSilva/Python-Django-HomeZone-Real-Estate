from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):


admin.site.register(Realtor, RealtorAdmin)
