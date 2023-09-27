from django.db import models

CURRENCY_CHOICES = (
    ("RUB", "Рубль"),
    ("USD", "Доллар"),
    ("EUR", "Евро"),
    ("CNY", "Юань")
)

class Shop(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название магазина')
    url = models.URLField(verbose_name="Ссылка", null=True, blank=True)
    address = models.CharField(max_length=128, verbose_name="Адрес магазина", null=True, blank=True)

class Brand(models.Model):
    name = models.CharField(max_length=32, verbose_name="Производитель")
    description = models.CharField(max_length=256, verbose_name="Информация о производителе", null=True, blank=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Список Производителей"
        ordering = ("-name",)

class Category(models.Model):
    name = models.CharField(max_length=48, verbose_name="Категория")
    description = models.CharField(max_length=256, verbose_name="Описание категории", null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Список категорий"
        ordering = ("-name",)

class BrandCategory(models.Model):
    brand = models.ForeignKey(Brand, verbose_name="Производитель", related_name="brands_categories", on_delete=models.CASCADE)
    category = models.ForeignKey(Brand, verbose_name="Категория", related_name="brands_categories", on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=48, verbose_name="Название продукта")
    category = models.ForeignKey(Category, verbose_name="Категория", blank=True,
                                 related_name="products", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Список продуктов"
        ordering = ("-name",)

class ProductInfo(models.Model):
    product = models.ForeignKey(Product, verbose_name="Продукт", related_name="product_info",
                                blank=True, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, verbose_name="Магазин", related_name="product_info", blank=True,
                             on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name="Производитель", related_name="products", blank=True,
                              on_delete=models.CASCADE)
    model = models.CharField(max_length=128, verbose_name="Производитель/Модель", null=True, blank=True)
    description = models.CharField(max_length=256, verbose_name="Описание", null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.PositiveIntegerField(verbose_name="Цена")
    currency = models.CharField(max_length=12, verbose_name="Валюта", choices=CURRENCY_CHOICES)

    class Meta:
        verbose_name = 'Информация о продукте'
        verbose_name_plural = "Информация о продуктах"
        constraints = [models.UniqueConstraint(fields=['product', 'shop'], name='unique_product_info')]

class Parameter(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя параметра")

    class Meta:
        verbose_name = 'Имя параметра'
        verbose_name_plural = "Список имен параметров"
        ordering = ('-name',)

class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, verbose_name="Информация о продукте",
                                     related_name="product_parameters", blank=True, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, verbose_name="Параметр", related_name="products_parameters",
                                  blank=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=64, verbose_name="Значение")
    measure_unit = models.CharField(max_length=24, verbose_name="Значение", null=True, blank=True)

