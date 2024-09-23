from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html', context=
                  {'message': 'OK'}, status=201)




