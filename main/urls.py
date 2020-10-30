from django.urls import path
from main import views


urlpatterns = [
    path('', views.search.as_view()) ,
    path('results/' , views.result_view.as_view() , name = 'results')
]