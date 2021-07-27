from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required


def blog(request):
    """ This view returns the blog page"""
    posts = Post.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts
    }

    return render(request, template, context)


def blog_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('blog_post', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_post.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_blog_post(request):
    """ Adds a blog post to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do add a blog post')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Could not add product to site. Please ensure form is valid!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
