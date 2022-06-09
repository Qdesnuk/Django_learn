from django.shortcuts import render
from django.http import *
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data('name')
            return HttpResponse(f'<h2> Имя {name} введено корректно </h2>')
        else:
            return HttpResponse('Ошибка ввода данных')
    else:
        userform = UserForm()
        return render(request, 'firstapp/index.html', context={"form": userform})


def about(request):
    return render(request, 'firstapp/about.html')


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
