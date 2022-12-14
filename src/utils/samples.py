from catalogue.models import Category, Order, Product, Subcategory


def sample_category(name):
    return Category.objects.create(name=name)


def sample_subcategory(name, category):
    return Subcategory.objects.create(name=name, category=category)


def sample_product(subcategory, name, price, **kwargs):
    defaults = {
        "code": 12345,
        "description": "Some test description",
        "in_stock": 1,
    }
    defaults.update(kwargs)
    return Product.objects.create(name=name, subcategory=subcategory, price=price, **defaults)


def sample_order(user, products):
    order = Order.objects.create(user=user)
    for product in products:
        order.generate_products_view.add(product)
    return order
