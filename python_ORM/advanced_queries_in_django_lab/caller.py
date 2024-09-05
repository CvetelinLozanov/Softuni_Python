import os
import django
from django.db import connection, reset_queries
from django.db.models import Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Order, OrderProduct, Customer, Category, Product


def product_quantity_ordered():
    total_quantity = Product.objects.annotate(
        total_quantity=Sum('orderproduct__quantity')
    ).exclude(total_quantity=None).order_by('-total_quantity')

    return '\n'.join(f'Quantity ordered of {p.name}: {p.total_quantity}' for p in total_quantity)


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
    #orders = OrderProduct.objects.select_related('order__customer', 'product__category').order_by('id')
    result = []

    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for ordered_product in order.orderproduct_set.all():
            result.append(f"- Product: {ordered_product.product.name}, Category: {ordered_product.product.category.name}")

    return '\n'.join(result)


def filter_products():
    available_products = Product.objects.filter(Q(price__gt=3.00) & Q(is_available=True)).order_by('-price', 'name')

    return '\n'.join(f"{p.name}: {p.price}lv." for p in available_products)


def give_discount():
    query = Q(price__gt=3.00) & Q(is_available=True)
    available_products = (Product.objects.filter(query)
                          .update(price=F('price') * 0.70))
    all_available_products = Product.objects.filter(is_available=True).order_by('-price', 'name')

    return '\n'.join(f"{p.name}: {p.price}lv." for p in all_available_products)


# print(give_discount())
# print(connection.queries)
