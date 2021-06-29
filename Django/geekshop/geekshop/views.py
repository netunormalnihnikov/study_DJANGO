from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = "магазин"
    products = Product.objects.all()[:3]
    links_tab = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'}
    ]
    context = {
        'title': title,
        'links_tab': links_tab,
        'products': products,
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
