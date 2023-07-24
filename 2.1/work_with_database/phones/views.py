from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort:
        if sort == 'max_price':
            phones = Phone.objects.order_by('-price')
        if sort == 'min_price':
            phones = Phone.objects.order_by('price')
        if sort == 'name':
            phones = Phone.objects.order_by('name')
    context['phones'] = phones
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone = Phone.objects.get(slug=slug)
    context['phone'] = phone
    return render(request, template, context)
