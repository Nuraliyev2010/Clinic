from django.urls import path
from . import views


urlpatterns =[
    # path('get_date_patient/', views.get_date_patient),
    # path('get_month_patient/', views.filter_pation_by_month),
    # # path('get_day_patient/', views.filter_pation_by_day),
    # # path('get_year_patient/', views.filter_pation_by_year),
    # path('get_month_report/', views.filter_report_by_month),
    path('all_patient/', views.all_employee),
    path('filter_employee_by_name/', views.filter_employee_by_name),
    path('filter_employee_by_expertise/', views.filter_emploee_by_expertise),
    path('filter_employee_by_status/', views.filter_emploee_by_status),
    path('filter_emploee_by_room/', views.filter_emploee_by_room),
    path('filter_amploee_by_time/', views.filter_amploee_by_time),
    path('filter_employee_by_section/', views.filter_employee_by_section),
    path('all_section/', views.all_section),
    path('all_class/', views.all_class),
    path('filter_capacity/', views.filter_capacity),
    path('filter_gender/', views.filter_gender),
]