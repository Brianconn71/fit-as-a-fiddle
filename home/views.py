from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


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

        send_mail(
            form.subject,
            form.message,
            form.email,
            ['brian.connolly71@gmail.com']
        )
        messages.success(request,
                            "Your message has been sent.\
                            A member of our customer service team will be in contact soon.")
        return redirect("home_")


