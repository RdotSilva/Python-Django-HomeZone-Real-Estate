from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

# Models
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    # Fetch listings, order by list date desc, filter by published only. [:3] limits it to 3 listings only
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:6]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Fetch all realtors ordered by hire date
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
