from django.shortcuts import render

from .models import Listing

# These method names match the 2nd argument in the urlpatterns list in urls.py
# views.index = index
# views.listing = listing


def index(request):
    # Fetch all of the listings
    listings = Listing.objects.all()

    # Create context to pass into the render method below
    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # Listing_id is passed in from the listings.html file when the link is clicked
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
