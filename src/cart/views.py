from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register

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
        cart_total = cart.get_total_price()

        return JsonResponse({'qty': cart_qty,
                             'subtotal': cart_total})


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_pk = request.POST.get('productpk')
        cart.delete(product=product_pk)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        return JsonResponse({'qty': cart_qty,
                             'subtotal': cart_total})


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_pk = int(request.POST.get('productpk'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_pk, qty=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        return JsonResponse({'qty': cart_qty,
                             'subtotal': cart_total})
