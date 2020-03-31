from django.shortcuts import render

# These method names match the 2nd argument in the urlpatterns list in urls.py
# views.index = index
# views.listing = listing


def index(request):
    render(request, 'listings/listings.html')


def listing(request):
    render(request, 'listings/listing.html')

