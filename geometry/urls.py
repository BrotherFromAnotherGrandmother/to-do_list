from django.urls import path, include
from . import views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area),
    path('square/<int:width>/', views.get_square_area),
    path('circle/<int:radius>/', views.get_circle_area),
    path('get_rectangle_area/<int:width>/<int:height>/', views.get_rectangle_area_by_get),
    path('get_square_area/<int:width>/', views.get_square_area_by_get),
    path('get_circle_area/<int:radius>/', views.get_circle_area_by_get),
]