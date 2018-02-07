from django.shortcuts import render


def index(request):
    title = 'Главная'
    content = {'title': title}

    return render(request, 'mainapp/index.html', content)
