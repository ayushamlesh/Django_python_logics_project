# created by me - -
# yaha pr logic of python likh rahe hai
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return HttpResponse('index.html')


def index2(request):
    age = request.GET.get('age')
    allow={}
    if age!="":
        age = int(age)
    elif age== "":
        allow = {"a": "give valid input"}
        return render(request, 'sum.html', allow)
    elif (age>60 or age < 15):
        allow = {"a": "not allowed"}
        return render(request, 'sum.html', allow)
    elif (age<=60 and age >= 15):
        allow={"a":"allowed"}
        return render(request, 'sum.html', allow)

