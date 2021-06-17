# Generated by Django 3.2.3 on 2021-06-15 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('no', models.IntegerField(blank=True, db_column='No', null=True)),
                ('street', models.CharField(blank=True, db_column='Street', max_length=255, null=True)),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('total', models.FloatField(blank=True, db_column='Total', null=True)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, db_column='Comment', max_length=255, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='Firstname', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='Lastname', max_length=255, null=True)),
            ],
            options={
                'db_table': 'fullname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('orderdate', models.DateField(blank=True, db_column='OrderDate', null=True)),
                ('total', models.FloatField(blank=True, db_column='Total', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=255, null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('orderid', models.IntegerField(db_column='OrderId')),
                ('paymethod', models.CharField(blank=True, db_column='PayMethod', max_length=255, null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('price', models.FloatField(blank=True, db_column='Price', null=True)),
                ('instock', models.IntegerField(blank=True, db_column='Instock', null=True)),
                ('rating', models.IntegerField(blank=True, db_column='Rating', null=True)),
                ('image', models.TextField(blank=True, db_column='Image', null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('shipdes', models.CharField(blank=True, db_column='ShipDes', max_length=255, null=True)),
                ('shipfee', models.FloatField(blank=True, db_column='ShipFee', null=True)),
            ],
            options={
                'db_table': 'shipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('tel', models.CharField(blank=True, db_column='Tel', max_length=255, null=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('author', models.CharField(blank=True, db_column='Author', max_length=255, null=True)),
                ('productid', models.OneToOneField(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BoECSystem.product')),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('brand', models.CharField(blank=True, db_column='Brand', max_length=255, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
                ('productid', models.OneToOneField(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BoECSystem.product')),
            ],
            options={
                'db_table': 'clothes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=255, null=True)),
                ('tel', models.CharField(blank=True, db_column='Tel', max_length=255, null=True)),
                ('userid', models.OneToOneField(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BoECSystem.user')),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('brand', models.CharField(blank=True, db_column='Brand', max_length=255, null=True)),
                ('productid', models.OneToOneField(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BoECSystem.product')),
            ],
            options={
                'db_table': 'electronic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('position', models.CharField(blank=True, db_column='Position', max_length=255, null=True)),
                ('salary', models.CharField(blank=True, db_column='Salary', max_length=255, null=True)),
                ('userid', models.OneToOneField(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BoECSystem.user')),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('productid', models.OneToOneField(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BoECSystem.product')),
            ],
            options={
                'db_table': 'product_cart',
                'managed': False,
            },
        ),
    ]
