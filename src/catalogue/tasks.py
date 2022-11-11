import random

from celery import shared_task
from faker import Faker

from catalogue.models import Category, Product, SubCategory


@shared_task
def generate_categories():
    category_names = ["Smartphones", "Tablets", "Laptops", "TVs", "Smart home", "Audio", "Accessories"]
    creation_list = []
    for category in category_names:
        data = {"name": category}
        creation_list.append(Category(**data))
    Category.objects.bulk_create(creation_list)


@shared_task
def generate_subcategories():
    fake = Faker()
    if not Category.objects.all():
        generate_categories()
    categories = Category.objects.all()
    creation_list = []
    for category in categories:
        for _ in range(5):
            data = {"category": category, "name": fake.word().title()}
            creation_list.append(SubCategory(**data))
    SubCategory.objects.bulk_create(creation_list)


@shared_task
def generate_products():
    fake = Faker()
    if not SubCategory.objects.all():
        generate_subcategories()
    subcategories = SubCategory.objects.all()
    creation_list = []
    for subcategory in subcategories:
        for _ in range(5):
            data = {
                "subcategory": subcategory,
                "name": fake.catch_phrase(),
                "code": random.randint(10_000, 99_999),
                "description": fake.text(1000),
                "price": random.randint(100, 10_000),
                "stock": random.randint(1, 10),
            }
            creation_list.append(Product(**data))
    Product.objects.bulk_create(creation_list)
