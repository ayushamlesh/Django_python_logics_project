# created by me - -
# yaha pr logic of python likh rahe hai
from ast import Return
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def forms(request):
    return render(request, 'form.html')


def calculate_ride(request):
    age = request.GET.get('age')
    name = request.GET.get('game')
    allow = {}
    if age == "":
        allow = {"a": "give valid input", "game_name": name}
        return render(request, 'ans.html', allow)
    if age != "":
        age = int(age)
    if (age > 60 or age < 15):
        allow = {"a": "not allowed"}
        return render(request, 'ans.html', allow)
    elif (age <= 60 and age >= 15):
        allow = {"a": "allowed", "game_name": name}
        return render(request, 'ans.html', allow)
