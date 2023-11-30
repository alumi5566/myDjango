from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .form import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data['email'])
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })
            send_mail("The contact", "This is the message", "123@this.com", ['alumi5566@gmail.com'], html_message=html)
            return HttpResponseRedirect(reverse("contact:index"))
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {
        'form': form
    })