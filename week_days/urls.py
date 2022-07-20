from django.urls import path
from . import views

urlpatterns = [
    path('<dayOfWeek>', views.get_the_day_of_the_week),
]
