from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return HttpResponse("Hello,dffdgdgdgdfgdgfx.")


def home(request):
    return render(request, 'home.html')


def blr(request):
    return render(request, 'banagalore.html')


def some_json(request):
    return JsonResponse({
        'status': 'success',
        'number': list(range(10))
    })


def drive_u(request):
    return render(request, 'DriveU.html')


def mywebsite(request):
    return render(request, template_name='mywebsite.html')
