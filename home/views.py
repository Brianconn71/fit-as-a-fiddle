from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    """ This view returns the index page"""

    return render(request, 'home/index.html')


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.subject = request.POST['subject'],
            form.message = request.POST['message'],
            form.email = request.POST['email'],
            form.save()
            messages.success(request,
                                    "Your message has been sent.\
                                    We will be in touch shortly.")
            return redirect("home")
        else:
            messages.error(request,
                                   'Error: something has gone wrong \
                                    please try again later.')
            return redirect('home')
    else:
        form = ContactForm()

    template = 'home/contact_us.html'
    context = {
        'form': form,
    }

    return render(request,
                  template,
                  context)
