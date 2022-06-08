from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    # return render(request, 'firstapp/home.html')
    # header = 'Персональные данные'
    # langs = ['Английский', 'Немецкий', 'Испанский']
    # user = {'name': 'Максим', 'age': 30}
    # addr = ('Виноградная', 23, 45)
    # data = {'header': header, 'langs': langs, 'user': user, 'address': addr}
    return render(request, 'firstapp/index.html')

def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponseRedirect('/about')


def details(request):
    return HttpResponsePermanentRedirect('/')


def products(request, product_id):
    category = request.GET.get('cat', '')
    output = f"<h2> Продукт № {product_id}  Категория: {category}"
    return HttpResponse(output)


def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Максим')
    output = f"<h2>Пользователь</h2><h3>id: {id} Имя: {name}</h3>"
    return HttpResponse(output)
