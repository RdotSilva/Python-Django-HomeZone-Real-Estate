from django.shortcuts import render


def contact(request):
    if request.method == 'POST':
        # Fetch the hidden fields
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
