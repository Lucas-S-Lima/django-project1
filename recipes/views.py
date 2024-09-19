from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context=
                  {'message': 'OK'}, status=201)


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return render(request, 'recipes/contato.html')




