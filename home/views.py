from django.shortcuts import render


def home(request):
    """ This view returns the index page"""

    return render(request, 'home/index.html')
