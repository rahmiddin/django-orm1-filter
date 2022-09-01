from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    filter_ = request.GET.get('sort')
    print(filter_)
    choice = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
    template = 'catalog.html'
    phones = Phone.objects.order_by(f'{choice[filter_]}')

    # if filter_:
    #     for key, value in choice.items():
    #         if filter_ == key:
    #             phones = Phone.objects.filter(f'{key}')
    # else:
    #     phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone}
    return render(request, template, context=context)