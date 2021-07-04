from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ This view returns all the products on the site with sorting and search queries too."""

    products = Product.objects.all()

    if request.GET:
        if 'search' in request.GET:

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ This view returns all the details of each individual item on the site from the product_id"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
