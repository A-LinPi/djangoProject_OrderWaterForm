from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
def index(req):
    return render(req, 'index.html')


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
