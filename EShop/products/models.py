from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60, db_index=True, verbose_name='назва')
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True, db_index=True, verbose_name='опис')
    manufacturer = models.ForeignKey('ProductManufacturer', on_delete=models.SET_NULL, null=True, db_index=True, verbose_name='виробник')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ціна')
    stock = models.PositiveIntegerField(verbose_name='на складі')
    is_active = models.BooleanField(default=False, verbose_name='продається')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавлення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товари'

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def admin_product_photo(self):
        """Надає можливість відобразити 'основне' фото обраного товару адмінці."""
        product_photo = ProductImage.objects.filter(product__id=self.id)[0]

        return mark_safe(f'<img src="/{product_photo.image_url}" width="100" />')

    admin_product_photo.short_description = 'фото продукту'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    image_url = models.ImageField(upload_to='static/products/product_images', verbose_name='посилання')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавлення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'фотографія'
        verbose_name_plural = 'фотографії'
        ordering = ['created_at']

    def admin_product_image(self):
        """Надає можливість відобразити всі фотографії обраного товару в адмінці."""
        return mark_safe(f'<img src="/{self.image_url}" width="150" />')

    admin_product_image.short_description = 'логотип'


class ProductManufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='назва')
    description = models.TextField(blank=True, verbose_name='опис')
    logo_url = models.ImageField(upload_to='static/products/logo_images', verbose_name='завантажити')

    def admin_manufacture_logo(self):
        """Надає можливість відобразити логотип виробника в адмінці."""
        return mark_safe(f'<img src="/{self.logo_url}" width="250" />')

    admin_manufacture_logo.short_description = 'логотип'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'виробник'
        verbose_name_plural = 'виробники'

# class Category(models.Model):
#     products = models.ManyToManyField(Product, related_name='products')
#     name = models.CharField(max_length=60, db_index=True)
#     short_desc = models.CharField(max_length=160, blank=True)
#     slug = models.SlugField(max_length=40, unique=True)
