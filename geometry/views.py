from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius ** 2}')


def get_rectangle_area_by_get(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}/')


def get_square_area_by_get(request, width):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}/')


def get_circle_area_by_get(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}/')