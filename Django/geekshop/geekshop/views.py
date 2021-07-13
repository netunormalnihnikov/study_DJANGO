from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = "магазин"
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    links_tab = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'}
    ]
    context = {
        'title': title,
        'links_tab': links_tab,
        'products': products,
        'basket': basket,
    }

    return render(request, "geekshop/index.html", context=context)


def contacts(request):
    title = "контакты"
    links_tab = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'}
    ]
    context = {
        'title': title,
        'links_tab': links_tab
    }
    return render(request, "geekshop/contact.html", context=context)
