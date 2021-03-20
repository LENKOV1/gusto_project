from django.urls import path
from .views import main_page_view, dish_page_view

urlpatterns = [
    path('', main_page_view, name='main_page_view'),
    path('menu/dish/<int:pk>', dish_page_view, name='dish_page_view')
]
