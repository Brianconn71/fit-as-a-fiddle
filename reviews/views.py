from django.shortcuts import render


# Add review view
def add_review(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(product_id=product.id)
