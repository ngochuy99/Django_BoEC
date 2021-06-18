from django.urls import path
from . import views

app_name = 'BoECSystem'

urlpatterns = [

    path('register', views.register, name='register'),

    path('login', views.login, name='login'),

    path('admin', views.admin_index, name="admin"),

    path('admin_add_new_product', views.admin_add_product, name="admin_add_new_product"),

    path('admin_remove_product/<int:remove_id>', views.admin_remove_product, name="admin_remove_product"),

    path('admin_update_product/<int:update_id>', views.admin_update_product, name="admin_update_product"),

    path('admin_verify_order', views.admin_verify_order, name="admin_verify_order"),

    path('admin_verify_order/<int:order_id>', views.admin_verify_order_detail, name="admin_verify_order_detail")

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
