from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Discount
from .forms import DiscountForm

# Discount apply form
@require_POST
def discount_apply(request):
    now = timezone.now()
    form = DiscountForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            discount = Discount.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
            request.session['discount_id'] = discount.id
        except Discount.DoesNotExist:
            request.session['discount_id'] = None
    return redirect('view_bag')