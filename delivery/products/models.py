from django.db import models



class Users(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full name', null=True, blank=False)
    username = models.CharField(max_length=50, verbose_name="username", null=True, unique=True)
    telegram_id = models.PositiveIntegerField(verbose_name="Telegram ID", unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, verbose_name="Product name")
    photo = models.CharField(verbose_name="Photo", max_length=255, null=True)
    price = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Descriptions", max_length=255, null=True)

    category_code = models.CharField(verbose_name="Category code", max_length=200)
    category_name = models.CharField(verbose_name="Cateegory name", max_length=50)
    subcategory_code = models.CharField(verbose_name="Ost category code", max_length=50)
    subcategory_name = models.CharField(verbose_name="Ost category name", max_length=50)

    def __str__(self):
        return f"{self.id} - {self.product_name}"


