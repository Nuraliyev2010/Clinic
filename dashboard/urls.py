from django.urls import path
from . import views

app_name = 'main'  # Define an app name if needed

urlpatterns = [
    # CRUD Employee URLs
    path('employee/create/', views.CreateEmploye.as_view(), name='create_employee'),
    path('employee/update/<int:pk>/', views.UpdateEmploye.as_view(), name='update_employee'),
    path('employee/delete/<int:pk>/', views.DeleteEmploye.as_view(), name='delete_employee'),

    # CRUD Section URLs
    path('section/create/', views.CreateSection.as_view(), name='create_section'),
    path('section/update/<int:pk>/', views.UpdateSection.as_view(), name='update_section'),
    path('section/delete/<int:pk>/', views.DeleteSection.as_view(), name='delete_section'),

    # CRUD Room URLs
    path('room/create/', views.CreateRoom.as_view(), name='create_room'),
    path('room/update/<int:pk>/', views.UpdateRoom.as_view(), name='update_room'),
    path('room/delete/<int:pk>/', views.DeleteRoom.as_view(), name='delete_room'),

    # CRUD Patient URLs
    path('patient/create/', views.CreatePatient.as_view(), name='create_patient'),
    path('patient/update/<int:pk>/', views.UpdatePatient.as_view(), name='update_patient'),
    path('patient/delete/<int:pk>/', views.DeletePatient.as_view(), name='delete_patient'),

    # CRUD Operation URLs
    path('operation/create/', views.CreateOperation.as_view(), name='create_operation'),
    path('operation/update/<int:pk>/', views.UpdateOperation.as_view(), name='update_operation'),
    path('operation/delete/<int:pk>/', views.DeleteOperation.as_view(), name='delete_operation'),

    # CRUD Info URLs
    path('info/create/', views.CreateInformation.as_view(), name='create_information'),
    path('info/update/<int:pk>/', views.UpdateInfprmation.as_view(), name='update_information'),
    path('info/delete/<int:pk>/', views.DeleteInformation.as_view(), name='delete_information'),

    # CRUD Cassa URLs
    path('cassa/create/', views.CreateCassa.as_view(), name='create_cassa'),
    path('cassa/update/<int:pk>/', views.UpdateCassa.as_view(), name='update_cassa'),
    path('cassa/delete/<int:pk>/', views.DeleteCassa.as_view(), name='delete_cassa'),

    # CRUD Report URLs
    path('report/create/', views.CreateReport.as_view(), name='create_report'),
    path('report/update/<int:pk>/', views.UpdateReport.as_view(), name='update_report'),
    path('report/delete/<int:pk>/', views.DeleteReport.as_view(), name='delete_report'),

    # CRUD Queue URLs
    path('queue/create/', views.CreateQueue.as_view(), name='create_queue'),
    path('queue/update/<int:pk>/', views.UpdateQueue.as_view(), name='update_queue'),
    path('queue/delete/<int:pk>/', views.DeleteQueue.as_view(), name='delete_queue'),

    # CRUD Attendance URLs
    path('attendance/create/', views.CreateAttendance.as_view(), name='create_attendance'),
    path('attendance/update/<int:pk>/', views.UpdateAttendance.as_view(), name='update_attendance'),
    path('attendance/delete/<int:pk>/', views.DeleteAttendance.as_view(), name='delete_attendance'),

    # CRUD Payment URLs
    path('payment/create/', views.CreatePayment.as_view(), name='create_payment'),
    path('payment/update/<int:pk>/', views.UpdatePayment.as_view(), name='update_payment'),
    path('payment/delete/<int:pk>/', views.DeletePayment.as_view(), name='delete_payment'),
]