from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента', min_length=2, max_length=20)
    age = forms.IntegerField(label='Возраст клиента', min_value=1, max_value=120)
    email = forms.EmailField(label='Электронный адрес')
    ad = forms.BooleanField(label='Согласны получать рекламу', required=False)
    # field_order = ['age', 'name']
    # basket = forms.BooleanField(label='Положить товар в корзину', required=False)
    # vyb = forms.NullBooleanField(label='Вы поедете в Сочи этим летом?')
    # email = forms.EmailField(label='Электронный адрес', help_text='Обязательный символ - @')
    # slug_text = forms.SlugField(label='Введите текст')
    # file = forms.FileField(label='Файл')
    # image = forms.ImageField(label='Изображение')
    # choice = forms.ChoiceField(choices=((1, 'Английский'), (2, 'Немецкий'), (3, 'Французский')), label='Выбор')
