from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from products.models import Product
from django.contrib import messages


# Add review view
# got a helping hand here https://www.youtube.com/watch?v=lSX8nzu9ozg
def add_review(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(product_id=product.id)
        if request.method == "POST":
            product = Product.objects.get(product_id=product.id)
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.reviewer = request.user
                review.title = request.POST['title']
                review.comment = request.POST['comment']
                review.rating = int(request.POST['rating'])
                review.product = product
                review.save()
                return redirect('product_details', product.id)
        else:
            form = ReviewForm()
        return render(request, 'reviews/reviews.html', {"form": form})
    else:
        messages.error(request,'Please sign in to leave a review')
        return redirect('account_login')

