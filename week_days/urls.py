from django.urls import path
from . import views

urlpatterns = [
    path('<int:dayOfWeek>', views.get_the_day_of_the_week_by_number),
    path('<str:dayOfWeek>', views.get_the_day_of_the_week, name='alias_for_the_day'),
]
