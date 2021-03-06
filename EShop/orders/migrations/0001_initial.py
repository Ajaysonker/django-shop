# Generated by Django 3.0.8 on 2020-08-02 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0008_auto_20200802_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(db_index=True, max_length=60, verbose_name="ім'я")),
                ('customer_phone', models.CharField(db_index=True, max_length=40, verbose_name='номер телефону')),
                ('customer_email', models.EmailField(blank=True, db_index=True, max_length=60, verbose_name='емейл')),
                ('customer_address', models.TextField(max_length=160, verbose_name='адреса')),
                ('comment', models.TextField(blank=True, max_length=240, verbose_name='коментар')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='дата заповнення')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='дата оновлення')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ціна')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='замовлення')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='товар')),
            ],
        ),
    ]
