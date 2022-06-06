from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2> Главная </h2>')

def about(request):
    return HttpResponse('<h2> О сайте </h2>')

def contact(request):
    return HttpResponse('<h2> Контакты </h2>')

def products(request, product_id = 1):
    output = f"<h2> Продукт № {product_id}"
    return HttpResponse(output)

def users(request, id=1, name='Максим'):
    output = f"<h2>Пользователь</h2><h3>id: {id} Имя: {name}</h3>"
    return HttpResponse(output)
