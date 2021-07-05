from django.shortcuts import render



def view_bag(request):
    """ This view returns the bag and its contents page"""

    return render(request, 'bag/bag.html')
