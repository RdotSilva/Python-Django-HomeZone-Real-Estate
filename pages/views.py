from django.shortcuts import render
from django.http import HttpResponse

# Models
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    # Fetch listings, order by list date desc, filter by published only. [:3] limits it to 3 listings only
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:6]
    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Fetch all realtors ordered by hire date
    realtors = Realtor.objects.order_by('-hire_date')
    return render(request, 'pages/about.html')
