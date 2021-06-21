from django.shortcuts import render, redirect
from BoEC.models import *
from datetime import date


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


def product_list(request):
    product = Product.objects.all()
    i = 1
    for x in product:
        x.price = int(x.price)
        x.pos = i
        i += 1
        if i == 7:
            i = 1
    return render(request, "shop/products.html", {"product": product})


def checkout(request):
    if request.method == "GET":
        cart = Cart.objects.get(customeruserid_id=request.session.get("user_id"),status="holding")
        user = User.objects.get(id=request.session.get("user_id"))
        customer = user.customer
        product_cart = ProductCart.objects.filter(cartid=cart)
        address = Address.objects.get(customeruserid=customer)
        i = 1
        for item in product_cart:
            item.pos = i
            i += 1
            if hasattr(item.productid, "book"):
                item.productType = "Book"
            if hasattr(item.productid, "clothes"):
                item.productType = "Clothes"
            if hasattr(item.productid, "electronic"):
                item.productType = "Electronics"
            item.productid.price = int(item.productid.price)
        cart.total = int(cart.total)
        return render(request, "shop/checkout.html",
                      {"product": product_cart, "cart": cart, "customer": customer, "address": address})
    if request.method == "POST":
        cart = Cart.objects.get(customeruserid_id=request.session.get("user_id"),status="holding")
        payment = request.POST.get("payMethod")
        shipment = request.POST.get("shipment")
        address = request.POST.get("address")
        city = request.POST.get("city")
        shipdes = address + ", " + city
        ship = Shipment(shipdes=shipdes, shipfee=20, shipname=shipment)
        ship.save()
        pay = Payment(cartid=cart, paymethod=payment,shipmentid=ship)
        pay.save()
        now = date.today()
        current_day = now.strftime("%d/%m/%Y")
        order = Order(customeruserid_id=request.session.get("user_id"), status="pending", total=cart.total,
                      orderdate=current_day, paymentid=pay)
        order.save()
        cart.status="done"
        cart.save()
        return redirect("/shop/index")


def add_product_to_cart(request, product_id):
    quantity = request.POST.get("quantity")
    cart_check = Cart.objects.filter(customeruserid=request.session.get("user_id"), status="holding").count()
    if cart_check == 0:
        product = Product.objects.get(id=product_id)
        cart = Cart(total=product.price*float(quantity), quantity=quantity, customeruserid_id=request.session.get("user_id"), status="holding")
        cart.save()
        product_cart = ProductCart(cartid=cart, productid=product, quantity=quantity)
        product_cart.save()
    elif cart_check != 0:
        cart = Cart.objects.get(customeruserid_id=request.session.get("user_id"), status="holding")
        product = Product.objects.get(id=product_id)
        cart.quantity += int(quantity)
        cart.total += float(product.price * float(quantity))
        cart.save()
        product_cart_check = ProductCart.objects.filter(productid=product, cartid=cart).count()
        if product_cart_check != 0:
            product_cart = ProductCart.objects.get(productid=product, cartid=cart)
            product_cart.quantity += int(quantity)
            product_cart.save()
        else:
            product_cart = ProductCart(cartid=cart, productid=product, quantity=quantity)
            product_cart.save()
    return redirect("/shop/product_detail/" + str(product_id))

def remove_from_cart(request,product_id):
    cart = Cart.objects.get(customeruserid_id=request.session.get("user_id"), status="holding")
    product_cart = ProductCart.objects.get(cartid=cart,productid_id=product_id)
    cart.quantity -= product_cart.quantity
    cart.total -= product_cart.quantity*product_cart.productid.price
    cart.save()
    product_cart.delete()
    return redirect("/shop/checkout")
