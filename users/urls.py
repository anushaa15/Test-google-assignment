from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path("login", views.login_view),
    path('reviews/', views.reviews_view),
    path('display/', views.display),
    path('homepage/', views.homepage, name="homepage"),
]