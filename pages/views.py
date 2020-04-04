from django.shortcuts import render
from django.http import HttpResponse

# Models
from listings.models import Listing


def index(request):
    # Fetch listings, order by list date desc, filter by published only. [:3] limits it to 3 listings only
    listings = Listing.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
