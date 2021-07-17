from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ This view returns all the products on the site with sorting and search queries too."""

    products = Product.objects.all()
    search = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "Please enter a search Criteria to search our products!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=search) | Q(description__icontains=search)
            products = products.filter(queries)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'current_categories': categories,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ This view returns all the details of each individual item on the site from the product_id"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def add_product(request):
    """ Adds a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Could not add product to site. Please ensure form is valid!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
