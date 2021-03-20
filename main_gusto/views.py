from django.shortcuts import render, redirect
from .models import *
from .forms import FormMessage

# Create your views here.

def main_page_view(request):

    if request.method == 'POST':
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    team_info = Team.objects.all().filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True).order_by('-category_order')
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True).order_by('dish_order')
        item.dishes = dishes

    special = Dish.objects.filter(category__title='Меню от шефа')
    form = FormMessage()

    return render(request, 'index.html', context={
            'categories': categories,
            'special': special,
            'team_info': team_info[0],
            'form': form,
        })


def dish_page_view(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish_info.html', context={'dish': dish})