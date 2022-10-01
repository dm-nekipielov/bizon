from catalogue.models import Category, Order, Product, SubCategory


def sample_category(name):
    return Category.objects.create(name=name)


def sample_subcategory(name, category):
    return SubCategory.objects.create(name=name, category=category)


def sample_product(subcategory, name, price, **kwargs):
    defaults = {
        "code": 12345,
        "description": "Some test description",
        "stock": 1,
    }
    defaults.update(kwargs)
    return Product.objects.create(name=name, subcategory=subcategory, price=price, **defaults)


def sample_order(user, products):
    order = Order.objects.create(user=user)
    for product in products:
        order.products.add(product)
    return order
