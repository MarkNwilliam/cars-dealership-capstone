from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt

from . import restapis
from .models import CarMake
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    try:
        User.objects.get(username=username)
        username_exist = True
    except User.DoesNotExist:
        logger.debug("{} is new user".format(username))
    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    else:
        data = {"userName": username, "error": "Already Registered"}
    return JsonResponse(data)


# Create a `get_cars` view to get car makes and models
def get_cars(request):
    count = CarMake.objects.filter().count()
    if (count == 0):
        initiate()
    car_models = restapis.get_cars()
    return JsonResponse({"CarModels": car_models})


# Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request, state=None):
    if request.method == "GET":
        state = state or request.GET.get('state', None)
        if state:
            dealerships = restapis.get_dealers_by_state(state)
        else:
            dealerships = restapis.get_dealers()
        context = {"status": 200, "dealers": dealerships}
        return JsonResponse(context)


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        reviews = restapis.get_dealer_reviews_from_mongodb(dealer_id)
        context = {"status": 200, "reviews": reviews}
        return JsonResponse(context)


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        dealership = restapis.get_dealer_by_id(dealer_id)
        context = {"status": 200, "dealer": dealership}
        return JsonResponse(context)


# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        try:
            response = restapis.post_review(data)
            return JsonResponse({"status": 200})
        except Exception:
            return JsonResponse({"status": 401}, status=401)
    else:
        return JsonResponse({"status": 403}, status=403)
