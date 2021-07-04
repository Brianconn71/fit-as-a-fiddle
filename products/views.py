from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ This view returns all the products on the site with sorting and search queries too."""

    products = Product.objects.all()
    search = None

    if request.GET:
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "Please enter a search Criteria to search our products!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=search) | Q(description__icontains=search)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': search,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ This view returns all the details of each individual item on the site from the product_id"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
