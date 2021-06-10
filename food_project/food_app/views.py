from django.http.response import HttpResponse
from django.shortcuts import render
from food_app.models import FoodDetails

# Create your views here.

def index(request):
    return render(request, "index.html")


def menu(request):
    breakfast = FoodDetails.objects.filter(category="Breakfast")
    lunch = FoodDetails.objects.filter(category="Lunch")
    dinner = FoodDetails.objects.filter(category="Dinner")
    return render(request,"menu.html", {"breakfast":breakfast, "lunch":lunch, "dinner":dinner})


def menu_details(request, food_id):
    details = FoodDetails.objects.filter(id = food_id)
    special = FoodDetails.objects.filter(category="Breakfast")
    return render(request, "menu-details.html", {'details':details, 'special':special})