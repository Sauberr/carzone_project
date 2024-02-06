from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this car')
                return redirect('/cars/' + car_id)
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
        last_name=last_name, email=email, phone=phone, customer_need=customer_need, city=city,
        state=state, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'Car Listing Inquiry',
            'There has been an inquiry for ' + car_title + '. Sign into the admin panel for more info',
            'email',
            [admin_email],
            fail_silently=False,
        )
        contact.save()
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/cars/' + car_id)
