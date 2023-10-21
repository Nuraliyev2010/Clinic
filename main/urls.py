from django.urls import path
from . import views


urlpatterns =[
    path('get_date_patient/', views.get_date_patient),
    path('get_month_patient/', views.filter_pation_by_month),
    path('get_day_patient/', views.filter_pation_by_day),
    path('get_year_patient/', views.filter_pation_by_year),
    path('get_year_/', views.filter_pation_by_year),
]