# Generated by Django 3.0.8 on 2020-07-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200727_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'фотографія', 'verbose_name_plural': 'фотографії'},
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='продається'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='static/products/images', verbose_name='посилання'),
        ),
    ]
