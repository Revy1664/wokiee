from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    """ Главная страница """

    return render(request, "dishes/index.html")


def categories_page_view(request):
    """ Страница со всеми категориями """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, "dishes/categories.html", context)


def category_products_page_view(request, slug):
    """ Страница с продуктами определённой категории """

    category = get_object_or_404(Category, slug=slug)
    products = Category.objects.get(slug=slug).product_set.all()

    context = {
        'category': category,
        'products': products,
    }

    return render(request, "dishes/products.html", context)


def product_detail_page_view(request, category_slug, product_slug):
    """ Страница детального просмотра продукта """
    
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug)
    similar_products = Category.objects.get(slug=category_slug).product_set.filter(~Q(slug=product_slug))

    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'category': category,
        'similar_products': similar_products,
        'cart_product_form': cart_product_form,
    }

    return render(request, "dishes/product_detail.html", context)
