# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customeruserid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerUserId')  # Field name made lowercase.
    no = models.IntegerField(db_column='No', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Book(models.Model):
    author = models.CharField(db_column='Author', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('Product', models.DO_NOTHING, db_column='ProductId', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey('Category', models.DO_NOTHING, db_column='CategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Cart(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customeruserid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerUserId')  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Clothes(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('Product', models.DO_NOTHING, db_column='ProductId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clothes'


class Comment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customeruserid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerUserId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductId')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class Customer(models.Model):
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    fullnameid = models.ForeignKey('Fullname', models.DO_NOTHING, db_column='FullnameId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Electronic(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('Product', models.DO_NOTHING, db_column='ProductId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electronic'


class Employee(models.Model):
    position = models.CharField(db_column='Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salary = models.CharField(db_column='Salary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    fullnameid = models.ForeignKey('Fullname', models.DO_NOTHING, db_column='FullnameId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Fullname(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fullname'


class Order(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customeruserid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerUserId')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentid = models.ForeignKey('Payment', models.DO_NOTHING, db_column='PaymentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Payment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderId')  # Field name made lowercase.
    paymethod = models.CharField(db_column='PayMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartId')  # Field name made lowercase.
    shipmentid = models.ForeignKey('Shipment', models.DO_NOTHING, db_column='ShipmentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    instock = models.IntegerField(db_column='Instock', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCart(models.Model):
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='ProductId', primary_key=True)  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartId')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cart'
        unique_together = (('productid', 'cartid'),)


class Shipment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shipdes = models.CharField(db_column='ShipDes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipfee = models.FloatField(db_column='ShipFee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment'


class Supplier(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
