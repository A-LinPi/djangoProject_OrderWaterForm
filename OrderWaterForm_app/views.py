from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here
def formcomment(req):
    nashaforma = UserComment()  # пустая форма
    data = {'forma': nashaforma}
    print(1)
    if req.POST:  # отправил форму
        nashaforma = UserComment(req.POST)  # форма с данными
        data = {'forma': nashaforma}
        print(2)
        if nashaforma.is_valid():
            print(3)
            k1 = nashaforma.cleaned_data.get('tel')
            k2 = nashaforma.cleaned_data.get('email')
            # k1 = req.POST.get('name')
            data = {'tel': k1, 'email': k2}
            return render(req, 'finish.html', data)

    return render(req, 'forma.html', data)


# Create your views here.
def index(req):
    return render(req, 'index.html')


def formaone(req):
    anketa = Forma1()
    if req.method == 'POST':
        k1 = req.POST.get('name')
        k2 = req.POST.get('age')
        out = f'<p>{k1}</p><p>{k2}</p>'
        return HttpResponse(out)
    else:
        data = {
            'forma': anketa
        }
    return render(req, 'forform.html', data)


# Create your views here.
def formatwo(req):
    anketa = Forma2()

    if req.POST:
        k1 = req.POST.get('name')
        k2 = req.POST.get('lastname')
        k3 = req.POST.get('email')
        k4 = req.POST.get('tel')
        k5 = req.POST.get('address')
        k6 = req.POST.get('month')
        k7 = req.POST.get('vol')

        data = {
            'forma': anketa,
            'k1': k1,
            'k2': k2,
            'k3': k3,
            'k4': k4,
            'k5': k5,
            'k6': k6,
            'k7': k7,
        }

        return render(req, 'order.html', data)
    else:
        data = {
            'forma': anketa
        }
    return render(req, 'forform.html', data)
