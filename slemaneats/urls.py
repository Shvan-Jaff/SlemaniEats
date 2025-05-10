
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_view, name='map'),
    path('categories/', views.categories, name='categories'),
]
