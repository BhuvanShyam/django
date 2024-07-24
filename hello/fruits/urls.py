from django.urls import path
from .import views
urlpatterns = [
    path('list/', views.fruit_list, name='fruit_list'),
]