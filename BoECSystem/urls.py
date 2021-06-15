from django.urls import path
from . import views

app_name = 'BoECSystem'

urlpatterns = [

    path('register', views.register, name='register'),

    path('login', views.login, name='login'),

    # path('index', views.index, name="index"),
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