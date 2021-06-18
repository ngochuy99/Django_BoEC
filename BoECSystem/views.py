from django.shortcuts import render, redirect
from BoEC.models import *


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = User.objects.get(username=username, password=password)
        if hasattr(user, "customer"):
            fullname = user.customer.fullnameid.firstname + " " + user.customer.fullnameid.lastname
            request.session["user"] = fullname
            request.session["role"] = "customer"
            request.session["user_id"] = user.id
            return redirect("../shop/index")
        elif hasattr(user, "employee"):
            fullname = user.employee.fullnameid.firstname + " " + user.employee.fullnameid.lastname
            request.session["user"] = fullname
            request.session["role"] = "admin"
            request.session["user_id"] = user.id
            return redirect("../boec/admin")
    return render(request, 'bookstore/login.html', {"status": "none"})


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("firstname", "")
        last_name = request.POST.get("lastname", "")
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        re_password = request.POST.get("re_password", "")
        district = request.POST.get("district", "")
        city = request.POST.get("city", "")
        street = request.POST.get("street", "")
        gender = request.POST.get("gender", "male")
        tel = request.POST.get("telephone")
        no = request.POST.get("no")
        age = request.POST.get("age")
        if password == re_password:
            user = User(username=username, password=password)
            user.save()
            fullname = Fullname(firstname=first_name, lastname=last_name)
            fullname.save()
            customer = Customer(type="normal", age=age, gender=gender, tel=tel, userid=user, fullnameid=fullname)
            customer.save()
            address = Address(no=no, street=street, district=district, city=city, customeruserid=customer)
            address.save()
            return render(request, 'bookstore/login.html', {"status": "none"})

    return render(request, 'bookstore/register.html', {"status": "none"})


def admin_index(request):
    product = Product.objects.all()
    i = 1
    for item in product:
        item.pos = i
        i += 1
        if hasattr(item, "book"):
            item.productType = "Book"
        if hasattr(item, "clothes"):
            item.productType = "Clothes"
        if hasattr(item, "electronic"):
            item.productType = "Electronics"
    return render(request, 'bookstore/admin.html', {"product": product})


def admin_remove_product(request, remove_id):
    product = Product.objects.get(id=remove_id)
    if hasattr(product, "book"):
        product.book.delete()
        product.delete()
    if hasattr(product, "clothes"):
        product.clothes.delete()
        product.delete()
    if hasattr(product, "electronic"):
        product.electronic.delete()
        product.delete()
    return redirect("../admin")


def admin_update_product(request, update_id):
    if request.method == "GET":
        product = Product.objects.get(id=update_id)
        supplier = Supplier.objects.all()
        category = Category.objects.all()
        if hasattr(product, "book"):
            book_type = "unset"
            electronic_type = "none"
            clothes_type = "none"
            product.productType = "Book"
        if hasattr(product, "clothes"):
            book_type = "none"
            electronic_type = "none"
            clothes_type = "unset"
            product.productType = "Clothes"
        if hasattr(product, "electronic"):
            book_type = "none"
            electronic_type = "unset"
            clothes_type = "none"
            product.productType = "Electronic"
        forward_att = {
            "book_type": book_type,
            "electronic_type": electronic_type,
            "clothes_type": clothes_type,
            "product": product,
            "category": category,
            "supplier": supplier
        }
        return render(request, "bookstore/adminUpdateProduct.html", forward_att)
    if request.method == "POST":
        productType = request.POST.get("productType", "")
        print(productType)
        productName = request.POST.get("productName", "")
        productPrice = request.POST.get("productPrice", 0)
        supplier = request.POST.get("productSupplier", 1)
        inStock = request.POST.get("inStock", 0)
        image = request.POST.get("imagePath", "")
        description = request.POST.get("description", "")
        product = Product.objects.get(id=update_id)
        if productType == "Book":
            author = request.POST.get("author", "")
            category = request.POST.get("productCategory")
            product.description = description
            product.name = productName
            product.price = productPrice
            product.supplierid_id = supplier
            product.instock = inStock
            product.image = image
            product.book.author = author
            product.book.categoryid_id = category
            product.save()
            product.book.save()
        elif productType == "Electronic":
            brand = request.POST.get("electronicsBrand", "")
            product.description = description
            product.name = productName
            product.price = productPrice
            product.supplierid_id = supplier
            product.instock = inStock
            product.image = image
            product.electronic.brand = brand
            product.save()
            product.electronic.save()
        elif productType == "Clothes":
            brand = request.POST.get("clothesBrand", "")
            clothesType = request.POST.get("clothesType", "")
            product.description = description
            product.name = productName
            product.price = productPrice
            product.supplierid_id = supplier
            product.instock = inStock
            product.image = image
            product.clothes.brand = brand
            product.clothes.type = clothesType
            product.save()
            product.clothes.save()
        return redirect("../admin")


def admin_add_product(request):
    if request.method == "GET":
        supplier = Supplier.objects.all()
        category = Category.objects.all()
        return render(request, 'bookstore/adminAddNewProduct.html', {'supplier': supplier, 'category': category})
    if request.method == "POST":
        productType = request.POST.get("productType", "")
        productName = request.POST.get("productName", "")
        productPrice = request.POST.get("productPrice", 0)
        supplier = request.POST.get("productSupplier", 1)
        inStock = request.POST.get("inStock", 0)
        image = request.POST.get("imagePath", "")
        description = request.POST.get("description", "")
        if productType == "book":
            author = request.POST.get("author", "")
            category = request.POST.get("productCategory")
            product = Product(supplierid_id=supplier,
                              name=productName,
                              price=productPrice,
                              instock=inStock,
                              image=image,
                              rating=0,
                              description=description)
            product.save()
            book = Book(productid=product, author=author, categoryid_id=category)
            book.save()
        elif productType == "electronic":
            brand = request.POST.get("electronicsBrand", "")
            product = Product(supplierid_id=supplier, name=productName, price=productPrice, instock=inStock,
                              image=image,
                              rating=0)
            product.save()
            electronic = Electronic(productid=product, brand=brand)
            electronic.save()
        elif productType == "clothes":
            brand = request.POST.get("clothesBrand", "")
            clothesType = request.POST.get("clothesType", "")
            product = Product(supplierid_id=supplier, name=productName, price=productPrice, instock=inStock,
                              image=image,
                              rating=0)
            product.save()
            clothes = Clothes(productid=product, brand=brand, type=clothesType)
            clothes.save()
        supplier = Supplier.objects.all()
        category = Category.objects.all()
        return render(request, 'bookstore/adminAddNewProduct.html', {'supplier': supplier, 'category': category})


def admin_verify_order(request):
    if request.method == "GET":
        order = Order.objects.all()
        return render(request, 'bookstore/adminVerifyOrder.html', {"order": order})


def admin_verify_order_detail(request, order_id):
    if request.method == "GET":
        order = Order.objects.get(id=order_id)
        cart = order.paymentid.cartid
        product_cart = ProductCart.objects.filter(cartid=cart)
        if order.status == "verified":
            status = "disabled"
        else:
            status = ""
        return render(request, "bookstore/adminVerifyOrderDetail.html", {"order": order, "product_cart": product_cart,"display":status})
    if request.method == "POST":
        order = Order.objects.get(id=order_id)
        cart = order.paymentid.cartid
        product_cart = ProductCart.objects.filter(cartid=cart)
        for x in product_cart:
            x.productid.instock -= x.quantity
            x.productid.save()
        order.status = "verified"
        order.save()
        return redirect("../admin_verify_order")


def check_role(request):
    if request.session.get("user") is None:
        return redirect("../login")
    else:
        if request.session.get("role") == "customer":
            return redirect("../index")
