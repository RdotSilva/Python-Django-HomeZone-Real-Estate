from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from secret import EMAIL_USER


def contact(request):
    if request.method == 'POST':
        # Fetch the hidden fields
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('listing', listing_id=listing_id)

        # Create the contact using the fields above
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        # Save contact to db
        contact.save()

        # Send email w/ title and body. Email will be sent to each email in the list [email, email, email]
        send_mail('Property Listing Inquiry', 'There has been an inquiry for ' + listing +
                  '. Sign into the Admin panel for more info.', EMAIL_USER, [realtor_email, EMAIL_USER], fail_silently=False)

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon!')

        # Redirect user to original listing page after form is submitted
        return redirect('listing', listing_id=listing_id)
