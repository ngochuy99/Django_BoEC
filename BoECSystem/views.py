from django.shortcuts import render
from BoECSystem.models import *


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = User.objects.get(username, password)
        print(user)
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
        if password == re_password:
            user = User(username=username, password=password)
            user.save()
            fullname = Fullname(firstname=first_name, lastname=last_name)
            fullname.save()
            # customer = Customer(type="normal",age=age,gender=gender,tel=tel,userid=user,fullnameid=fullname)
            # customer.save()
            # address = Address(no=no,street=street,district=district,city=city,customeruserid=customer)
            # address.save()

    return render(request, 'bookstore/register.html', {"status": "none"})
