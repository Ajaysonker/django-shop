# Generated by Django 3.1 on 2020-08-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200808_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=160, null=True, verbose_name='адреса'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=60, null=True, verbose_name='емейл'),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(db_index=True, max_length=60, null=True, verbose_name="ім'я"),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(db_index=True, max_length=60, null=True, verbose_name='прізвище'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(db_index=True, max_length=40, null=True, verbose_name='номер телефону'),
        ),
    ]
