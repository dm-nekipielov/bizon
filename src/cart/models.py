from decimal import Decimal

from catalogue.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("skey")
        if "skey" not in request.session:
            cart = self.session["skey"] = {}
        self.cart = cart

    def add(self, product, qty):
        product_pk = str(product.pk)

        if product_pk in self.cart:
            self.cart[product_pk]["qty"] = qty
        else:
            self.cart[product_pk] = {
                "price": str(product.price),
                "qty": int(qty),
            }
        self.save()

    def __iter__(self):
        product_pks = self.cart.keys()
        products = Product.objects.filter(pk__in=product_pks)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.pk)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    def delete(self, product):
        product_pk = str(product)
        if product_pk in self.cart:
            del self.cart[product_pk]
            self.save()

    def update(self, product, qty):
        product_pk = str(product)
        if product_pk in self.cart:
            self.cart[product_pk]["qty"] = qty
        self.save()

    def save(self):
        self.session.modified = True
