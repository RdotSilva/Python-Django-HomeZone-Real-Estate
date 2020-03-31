from django.urls import path

from . import views

# The 2nd argument of the path in the urlpatterns should match the method names created inside views.py
# views.index = index
# views.listing = listing


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
