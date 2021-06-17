from django.shortcuts import render, redirect
from BoEC.models import *


# Create your views here.


def index(request):
    product = Product.objects.order_by("-instock")
    i = 1
    product = product[0:6]
    for x in product:
        x.pos = i
        i += 1
    return render(request, "shop/index.html", {"product": product})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    product.price = int(product.price)
    productList = Product.objects.order_by("?")
    i = 1
    productList = productList[0:3]
    for x in productList:
        x.pos = i
        x.price = int(x.price)
        i += 1
    return render(request, "shop/productDetails.html", {"product": product, "productList": productList})


def add_product_to_cart(request, product_id):
    quantity = request.POST.get("quantity")
    cart_check = Cart.objects.filter(customeruserid=request.session.get("user_id")).count()
    if cart_check == 0:
        cart = Cart(total=0, quantity=0, customeruserid_id=request.session.get("user_id"))
        cart.save()
        product = Product.objects.get(id=product_id)
        product_cart = ProductCart(cartid=cart, productid=product, quantity=quantity)
        product_cart.save()
    elif cart_check != 0:
        cart = Cart.objects.get(customeruserid_id=request.session.get("user_id"))
        product = Product.objects.get(id=product_id)
        cart.quantity += int(quantity)
        cart.total += float(product.price * float(quantity))
        cart.save()
        product_cart_check = ProductCart.objects.filter(productid=product,cartid=cart).count()
        if product_cart_check != 0:
            product_cart = ProductCart.objects.get(productid=product,cartid=cart)
            product_cart.quantity += int(quantity)
            product_cart.save()
        else:
            product_cart = ProductCart(cartid=cart, productid=product, quantity=quantity)
            product_cart.save()
    return redirect("/shop/product_detail/" + str(product_id))
