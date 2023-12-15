from django.shortcuts import render, redirect
from django.contrib.auth import logout
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Create your views here.

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def get_google_reviews(api_key, place_id):
    credentials = service_account.Credentials.from_service_account_file(
        'googleint\client_secret_262412333177-kiq9m3cbr5o37bp1iuhlc3v2pmo88924.apps.googleusercontent.com.json',
        scopes=['https://www.googleapis.com/auth/business.manage']
    )

    service = build('mybusiness', 'v4', credentials=credentials)

    # Specify the location ID for the business
    location_name = f'locations/{place_id}'

    # Retrieve reviews
    reviews = service.accounts().locations().reviews().list(name=location_name).execute()

    return reviews.get('reviews', [])

def reviews_view(request):
    api_key = 'AIzaSyB-8UdzViq3WzTZlPfFyW7MOG7oApMu91I'
    place_id = 'place-id'

    google_reviews = get_google_reviews(api_key, place_id)

    return render(request, 'reviews.html', {'google_reviews': google_reviews})