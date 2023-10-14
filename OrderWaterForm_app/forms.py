from django import forms
from django.core.validators import RegexValidator

class Forma2(forms.Form):
    MONTHS = (('один месяц', '1 мес'),
              ('три месяца', '3 мес'),
              ('шесть месяцев', '6 мес'),
              ('двенадцать месяцев', '12 мес'))
    VOL = (('5 литров', '5л'),
           ('10 литров', '10л'),
           ('15 литров', '15л'))
    name = forms.CharField(max_length=20, label='Имя')
    lastname = forms.CharField(max_length=30, label='Фамилия')
    email = forms.EmailField(required=False, validators=[
        RegexValidator('^[A-Za-z0-9_]{1,100}(@){1}(mail.ru){1}$', message='неправильный email')
    ])
    tel = forms.CharField(label='телефон', validators=[RegexValidator('^[+][7]{1}[0-9]{10}$', message='неправильный телефон')])
    address = forms.CharField(label='Адрес')
    month = forms.ChoiceField(label='Количество месяцев доставки воды', choices=MONTHS)
    vol = forms.ChoiceField(label='Объём баллона воды', choices=VOL)
