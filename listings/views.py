from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# These method names match the 2nd argument in the urlpatterns list in urls.py
# views.index = index
# views.listing = listing


def index(request):
    # Fetch all of the listings ordered by list date desc. Filter results to published only.
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Pagination
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # Create context to pass into the render method below
    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # Listing_id is passed in from the listings.html file when the link is clicked
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
