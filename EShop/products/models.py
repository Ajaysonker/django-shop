from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60, null=True, db_index=True, verbose_name='назва')
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True, db_index=True, verbose_name='опис')
    manufacturer = models.ForeignKey('ProductManufacturer', on_delete=models.SET_NULL, null=True, db_index=True,
                                     verbose_name='виробник')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ціна')
    stock = models.PositiveIntegerField(null=True, verbose_name='на складі')
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
        return mark_safe(f'<img src="{product_photo.imageURL}" width="100" />')

    admin_product_photo.short_description = 'фото продукту'


def product_image_uploader(instance, filename):
    return f'static/products/images/{instance.product.manufacturer.name}/{instance.product.id}/{filename}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    image = models.ImageField(upload_to=product_image_uploader, verbose_name='посилання', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавлення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата оновлення')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'фотографія'
        verbose_name_plural = 'фотографії'
        ordering = ['created_at']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def admin_product_image(self):
        """Надає можливість відобразити всі фотографії обраного товару в адмінці."""
        return mark_safe(f'<img src="{self.imageURL}" width="150" />')

    admin_product_image.short_description = 'логотип'


class ProductManufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='назва')
    description = models.TextField(blank=True, verbose_name='опис')
    logo = models.ImageField(upload_to='static/products/images/manufacturer_logo/', verbose_name='завантажити', blank=True,
                             null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'виробник'
        verbose_name_plural = 'виробники'

    @property
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url

    def admin_manufacture_logo(self):
        """Надає можливість відобразити логотип виробника в адмінці."""
        return mark_safe(f'<img src="{self.logoURL}" width="250" />')

    admin_manufacture_logo.short_description = 'логотип'

# class Category(models.Model):
#     products = models.ManyToManyField(Product, related_name='products')
#     name = models.CharField(max_length=60, db_index=True)
#     short_desc = models.CharField(max_length=160, blank=True)
#     slug = models.SlugField(max_length=40, unique=True)
