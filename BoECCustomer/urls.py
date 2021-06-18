from django.urls import path
from . import views

app_name = 'BoECCustomer'

urlpatterns = [

    path('index', views.index, name="index"),

    path('product_detail/<int:product_id>', views.product_detail, name="product_detail"),

    path('add_product_to_cart/<int:product_id>',views.add_product_to_cart,name = "add_product_to_cart"),

    path('product_list',views.product_list,name="product_list"),

    path('checkout', views.checkout, name="checkout"),

    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name="remove_from_cart")

    #
    # path('book', views.getbook, name="getbook"),
    #
    # path('electronics', views.getElectronics, name="getElectronics"),
    #
    # path('clothes', views.getClothes, name="getClothes"),
    #
    # path('addcart/<str:type>/<int:id>', views.addcart),
    #
    # path('addtocart/<str:type>/<int:id>', views.addtocart),
    #
    # path('pay', views.pay),
    #
    # path('saveorder', views.saveorder)

]
