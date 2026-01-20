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
    dealerships = []
    for i in range(1, 51):
        state = "Kansas" if i % 2 == 0 else "Texas"
        st = "KS" if i % 2 == 0 else "TX"
        dealerships.append({
            "id": i,
            "city": "City " + str(i),
            "state": state,
            "st": st,
            "address": str(i*100) + " Main St",
            "zip": "7990" + str(i % 10),
            "lat": 31.7,
            "long": -106.4,
            "short_name": "Dealer" + str(i),
            "full_name": "Full Dealer Name " + str(i)
        })
    return JsonResponse({"dealerships": dealerships})

def get_dealerships_by_state(request, state):
    dealerships = []
    for i in range(1, 51):
        s = "Kansas" if i % 2 == 0 else "Texas"
        if s.lower() == state.lower():
            st = "KS" if i % 2 == 0 else "TX"
            dealerships.append({
                "id": i,
                "city": "City " + str(i),
                "state": s,
                "st": st,
                "address": str(i*100) + " Main St",
                "zip": "7990" + str(i % 10),
                "lat": 31.7,
                "long": -106.4,
                "short_name": "Dealer" + str(i),
                "full_name": "Full Dealer Name " + str(i)
            })
    return JsonResponse({"dealerships": dealerships})

def get_dealer_details(request, dealer_id):
    dealer = {
        "id": dealer_id,
        "city": "City " + str(dealer_id),
        "state": "Kansas",
        "st": "KS",
        "address": str(dealer_id*100) + " Main St",
        "zip": "79901",
        "lat": 31.7,
        "long": -106.4,
        "short_name": "Dealer" + str(dealer_id),
        "full_name": "Full Dealer Name " + str(dealer_id)
    }
    return JsonResponse({"dealer": dealer})

def get_dealer_reviews(request, dealer_id):
    reviews = [
        {"id": 1, "name": "John Doe", "dealership": dealer_id, "review": "Great service!", "purchase": True, "purchase_date": "2023-01-01", "car_make": "Audi", "car_model": "A6", "car_year": 2010},
    ]
    return JsonResponse({"reviews": reviews})

def get_cars(request):
    car_models = [
         {"car_make": "Audi", "car_model": "A6"},
         {"car_make": "BMW", "car_model": "X5"},
         {"car_make": "Toyota", "car_model": "Camry"},
    ]
    return JsonResponse({"CarModels": car_models})

def analyze_review(request, text):
     if "Fantastic" in text:
         return JsonResponse({"sentiment": "positive"})
     return JsonResponse({"sentiment": "neutral"})
