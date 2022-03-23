from email import message
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from Email_App.forms import RegisterForm
from django.conf import settings
from .models import *
from django.contrib import messages


def index(request):

    return render(request, 'index.html')


def User_register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            username = request.POST['username']
            email = request.POST['email']

            mydict = {'username': username}

            html_template = 'register_email.html'
            html_message = render_to_string(html_template, context=mydict)

            subject = 'welcome to BooksApp'

            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            message = EmailMessage(subject, html_message,
                                   from_email, recipient_list)
            message.content_subtype = 'html'
            message.send()

            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username} ! check your mail-box')

            form.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
