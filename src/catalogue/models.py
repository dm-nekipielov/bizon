from enum import unique

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Product(models.Model):
    subcategory = models.ForeignKey(to="catalogue.Subcategory", related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    code = models.IntegerField(null=True)
    image = models.ImageField(upload_to="catalogue/products/%Y/%m/%d", default="/media/catalogue/no_image.jpg")
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("catalogue:product", args=[self.slug])

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(to="catalogue.Category", related_name="subcategories", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="catalogue/subcategory/%Y/%m/%d", default="/media/catalogue/no_image.jpg")
    name = models.CharField(max_length=512, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def get_absolute_url(self):
        return reverse("catalogue:subcategory", args=[self.slug])

    def __str__(self):
        return f"{self.id} {self.name}"


class Category(models.Model):
    image = models.ImageField(upload_to="catalogue/category/%Y/%m/%d", default="/media/catalogue/no_image.jpg")
    name = models.CharField(max_length=512, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("catalogue:category", args=[self.slug])

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    product = models.ForeignKey(to=Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name="user_comments", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=1024)


class Order(models.Model):
    user = models.ForeignKey(to=get_user_model(), related_name="user_orders", on_delete=models.CASCADE)
    products = models.ManyToManyField(
        to=Product,
        related_name="orders",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def total(self):
        return sum(i.price for i in self.products.all())


# class Wishlist(models.Model):
#     ...
#
#     def __str__(self):
#         return self.wished_item.title
