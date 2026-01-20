from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

def logout_user(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

def get_dealerships(request):
    dealerships = [
        {"id": 1, "city": "El Paso", "state": "Texas", "st": "TX", "address": "123 Main St", "zip": "79901", "lat": 31.7, "long": -106.4, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership"},
        {"id": 2, "city": "Minneapolis", "state": "Kansas", "st": "KS", "address": "456 Oak St", "zip": "55401", "lat": 44.9, "long": -93.2, "short_name": "Nursery", "full_name": "Nursery Car Dealership"},
        {"id": 3, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "789 Pine St", "zip": "66601", "lat": 39.0, "long": -95.6, "short_name": "Topeka Dealers", "full_name": "Topeka Dealership"},
    ]
    return JsonResponse({"dealerships": dealerships})

def get_dealerships_by_state(request, state):
    dealerships = [
        {"id": 2, "city": "Minneapolis", "state": "Kansas", "st": "KS", "address": "456 Oak St", "zip": "55401", "lat": 44.9, "long": -93.2, "short_name": "Nursery", "full_name": "Nursery Car Dealership"},
        {"id": 3, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "789 Pine St", "zip": "66601", "lat": 39.0, "long": -95.6, "short_name": "Topeka Dealers", "full_name": "Topeka Dealership"},
    ]
    # Simple filter mock
    if state == "Kansas":
         return JsonResponse({"dealerships": dealerships})
    return JsonResponse({"dealerships": []})

def get_dealer_details(request, dealer_id):
    dealer = {"id": 1, "city": "El Paso", "state": "Texas", "st": "TX", "address": "123 Main St", "zip": "79901", "lat": 31.7, "long": -106.4, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership"}
    if dealer_id == 1:
        return JsonResponse({"dealer": dealer})
    return JsonResponse({"dealer": {}})

def get_dealer_reviews(request, dealer_id):
    reviews = [
        {"id": 1, "name": "John Doe", "dealership": 1, "review": "Great service!", "purchase": True, "purchase_date": "2023-01-01", "car_make": "Audi", "car_model": "A6", "car_year": 2010},
    ]
    if dealer_id == 1:
        return JsonResponse({"reviews": reviews})
    return JsonResponse({"reviews": []})

def get_cars(request):
    cars = [
         {"id": 1, "name": "Audi", "description": "German car", "models": [{"name": "A6", "type": "Sedan", "year": 2023}]},
         {"id": 2, "name": "BMW", "description": "German car", "models": [{"name": "X5", "type": "SUV", "year": 2023}]},
    ]
    return JsonResponse({"cars": cars})

def analyze_review(request):
    if request.method == 'GET':
         text = request.GET.get('text', '')
         if "Fantastic" in text:
             return JsonResponse({"sentiment": "positive"})
         return JsonResponse({"sentiment": "neutral"})
    return JsonResponse({"sentiment": "unknown"})
