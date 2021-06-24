from django.shortcuts import render


def index(request):
    title = "магазин"
    links_tab = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'}
    ]
    context = {
        'title': title,
        'links_tab': links_tab
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
