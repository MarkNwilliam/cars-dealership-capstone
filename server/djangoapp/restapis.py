import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    print("GET from {} ".format(endpoint))
    try:
        response = requests.get(endpoint, params=kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return {}


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return {}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return {}


def get_dealers():
    url = backend_url + "/fetchDealers"
    json_result = get_request(url)
    dealers = json_result
    return dealers


def get_dealers_by_state(state):
    url = backend_url + "/fetchDealers/" + state
    json_result = get_request(url)
    dealers = json_result
    return dealers


def get_dealer_by_id(dealer_id):
    url = backend_url + "/fetchDealer/" + str(dealer_id)
    json_result = get_request(url)
    dealer = json_result
    return dealer


def get_dealer_reviews_from_mongodb(dealer_id):
    url = backend_url + "/fetchReviews/dealer/" + str(dealer_id)
    json_result = get_request(url)
    reviews = json_result
    if reviews:
        for review in reviews:
            if 'sentiment' not in review:
                sentiment = analyze_review_sentiments(review['review'])
                review['sentiment'] = sentiment.get('sentiment', 'neutral')
    return reviews


def get_cars():
    car_list = []
    from .models import CarMake, CarModel
    makes = CarMake.objects.all()
    for make in makes:
        models = CarModel.objects.filter(car_make=make)
        for model in models:
            car_list.append({"CarMake": make.name, "CarModel": model.name})
    return car_list
