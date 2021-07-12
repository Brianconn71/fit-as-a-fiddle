from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Checkout view rendered to website
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You currently have no bag items")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J41AKJlYwbBfggKoPYVxYOOHm4Q78kltZxae5z3BZlP7epmydxbwYprNB3VeMRoaJs4Hy1ew15TgC0azwJuqRf9000QM0ExHG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
