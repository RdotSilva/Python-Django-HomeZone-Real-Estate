from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

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

    # Check for listing otherwise return 404 error
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords search field
    # Using "icontains" to check entire paragraph for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)
