from django.shortcuts import render

# These method names match the 2nd argument in the urlpatterns list in urls.py
# views.index = index
# views.listing = listing


def index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
