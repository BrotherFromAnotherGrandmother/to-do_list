from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius ** 2}')


def get_rectangle_area_by_get(request, width, height):
    redirect_url = reverse('rectangle', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square_area_by_get(request, width):
    redirect_url = reverse('square', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area_by_get(request, radius):
    redirect_url = reverse('circle', args=(radius,))
    return HttpResponseRedirect(redirect_url)