from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User
from products.models import Product
from django.contrib import messages


# Add review view
# got a helping hand here https://www.youtube.com/watch?v=lSX8nzu9ozg
@login_required
def add_review(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in members may leave a review')
        return redirect(reverse('home'))

    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
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


@login_required
def edit_review(request, review_id):
    """ edits a product on the site """
    if review.user != request,user:
        messages.error(request, 'Sorry, you do not have the required permissions to do this')
        return redirect(reverse('product_details', product.id))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, f'Failed to update {product.name}. Please ensure form is valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
