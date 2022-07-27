from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_the_day_of_the_week(request, dayOfWeek):
    dictionary_of_days_of_the_week = {
        'monday': 'в понедельник я жалею себя',
        'tuesday': 'во вторник - глазею в пропасть',
        'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
        'thursday': 'в четверг - зарядка',
        'friday': 'ужин с собой, нельзя снова его пропускать',
        'saturday': 'в субботу - борьба с презрением к себе',
        'sunday': 'в воскресенье - иду на рождество'
    }
    if dayOfWeek in dictionary_of_days_of_the_week:
        return HttpResponse(dictionary_of_days_of_the_week[dayOfWeek])
    else:
        return HttpResponse('Такого дня нет')


def get_the_day_of_the_week_by_number(request, dayOfWeek: int):
    if 1 <= dayOfWeek <= 7:
        return HttpResponse(f'Сегодня {dayOfWeek} день недели')
    return HttpResponse(f'Неверный номер дня - {dayOfWeek}')
