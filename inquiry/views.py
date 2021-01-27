from django.shortcuts import render, redirect
from .models import Inquiry
from django.contrib import messages
# from django.core.mail import send_mail


def inquiry(request):
    if request.method == 'POST':
        # get the fields
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry on a particular listing
        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Inquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if has_inquired:
                messages.error(request, 'You have made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        inquiry = Inquiry(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)

        inquiry.save()

        # send mail
        # send_mail(
        #     'Property Listing Inquiry for {}'.format(listing),
        #     'Listing inquiry for {}'.format(listing),
        #     'retry2067@gmail.com',
        #     [realtor_email, 'macmive@gmail.com', 'omive@yahoo.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Message sent, you will be contacted shortly')
        return redirect('/listings/'+listing_id)

