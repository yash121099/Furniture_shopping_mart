from django.shortcuts import render, redirect
from .models import Client
from django.contrib import messages
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib.auth.models import auth


# Create your views here.

def login(request):
    if request.session.get("fullname") or request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            client = Client.objects.get(email=email, password=password)
            if client.status == "active":
                request.session['fullname'] = client.fullname
                request.session['clientpk'] = client.pk
                return redirect("/")
            else:
                messages.info(request, "Complete OTP Confirmation")
                return redirect("/accounts/otp")
        except:
            messages.info(request, "Enter correct credentials")
            return redirect("/accounts/login")
    else:
        return render(request, "accounts/login.html")


def signup(request):
    if request.session.get("fullname") or request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")

        if Client.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("/accounts/signup")
        else:
            Client.objects.create(fullname=fullname, email=email, mobile=mobile, password=password)

            rec = [email, ]
            subject = "Succesfull OTP registeration"
            random_otp = random.randint(1000, 9999)
            message = "Your OTP for successfull registeration is " + str(random_otp)
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, rec)

            request.session['random_otp'] = random_otp
            request.session['email'] = email
            return redirect("/accounts/otp")
            # return render(request, 'accounts/otp.html', {'random_otp': random_otp, 'email': email})
    else:
        return render(request, "accounts/signup.html")


def logout_req(request):
    try:
        del request.session['fullname']
        del request.session['clientpk']
        logout(request)
        return redirect("/")
    except:
        auth.logout(request)
        return redirect("/")


def otp(request):
    if request.session.get("fullname") or request.user.is_authenticated:
        return redirect("/")

    return render(request, "accounts/otp.html")


def validateotp(request):
    if request.session.get("fullname") or request.user.is_authenticated:
        return redirect("/")

    error = ""
    if request.method == "POST":
        email = request.POST['email']
        random_otp = request.POST['random_otp']
        user_otp = request.POST['user_otp']

        if random_otp == user_otp:
            client = Client.objects.get(email=email)
            client.status = "active"
            client.save()

            del request.session['email']
            del request.session['random_otp']

            return redirect("/accounts/login")
        else:
            messages.info(request, "Enter correct OTP")
            return redirect("/accounts/otp")
            # message = "Enter correct OTP"
            # return render(request, 'accounts/otp.html', {'random_otp': random_otp, 'message':message, 'email': email})
    else:
        return redirect("/")


def resend(request):
    if request.session.get("fullname") or request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST['email']
        rec = [email, ]
        subject = "Succesfull OTP registeration"
        random_otp = random.randint(1000, 9999)
        message = "Your OTP for successfull registeration is " + str(random_otp)
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, rec)
        request.session['random_otp'] = random_otp
        return redirect("/accounts/otp")
        # return render(request, 'accounts/otp.html', {'random_otp': random_otp, 'email': email})
    else:
        return redirect("/")

    # rec = [email, ]
    # subject = "Succesfull OTP registeration"
    # random_otp = random.randint(1000, 9999)
    # message = "Your OTP for successfull registeration is " + str(random_otp)
    # email_from = settings.EMAIL_HOST_USER
    # send_mail(subject, message, email_from, rec)
    # return render(request, 'accounts/otp.html', {'random_otp': random_otp, 'email': email})
