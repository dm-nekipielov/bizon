from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from cart.models import Cart
from catalogue.models import Product


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'store/cart.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_pk = request.POST.get('productpk')
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, pk=product_pk)
        cart.add(product=product, qty=product_qty)
        cart_qty = cart.__len__()
        return JsonResponse({'qty': cart_qty})

#TODO: timestamp 02:58:13