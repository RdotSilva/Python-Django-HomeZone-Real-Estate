from django.shortcuts import render


def contact(request):
    if request.method == 'POST':
        # Fetch the hidden fields
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
