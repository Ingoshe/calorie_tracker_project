from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import FoodItem

# Create your views here.


def food_list(request):
    foods = FoodItem.objects.all()
    total_calories = sum(food.calorie_count for food in foods)
    context = {
        'foods': foods,
        'total_calories': total_calories,
    }
    return render(request, 'food_list.html', context)

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calorie_count = request.POST['calorie_count']
        FoodItem.objects.create(name=name, calorie_count=calorie_count)
        return redirect('food_list')
    return render(request, 'add_food.html')

def delete_food(request, food_id):
    FoodItem.objects.filter(id=food_id).delete()
    return redirect('food_list')

def reset_calories(request):
    FoodItem.objects.all().delete()
    return redirect('food_list')
