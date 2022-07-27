from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
dictionary_of_days_of_the_week = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday': 'в четверг - зарядка',
    'friday': 'ужин с собой, нельзя снова его пропускать',
    'saturday': 'в субботу - борьба с презрением к себе',
    'sunday': 'в воскресенье - иду на рождество'
}

def get_the_day_of_the_week(request, dayOfWeek):
    if dayOfWeek in dictionary_of_days_of_the_week:
        return HttpResponse(dictionary_of_days_of_the_week[dayOfWeek])
    else:
        return HttpResponse('Такого дня нет')


def get_the_day_of_the_week_by_number(request, dayOfWeek: int):
    list_days_of_week = list(dictionary_of_days_of_the_week)
    if 1 <= dayOfWeek <= 7:
        day_of_the_week = list_days_of_week[dayOfWeek-1]
        redirect_url = reverse('alias_for_the_day', args=(day_of_the_week, ))
        return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'Неверный номер дня - {dayOfWeek}')
