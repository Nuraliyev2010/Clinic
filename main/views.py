from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from datetime import datetime, timedelta

# @api_view(['GET'])
# def get_date_patient(request):
#     created_at = request.GET.get('created_at')
#     created = Patient.objects.filter(created_at=created_at)
#     ser = PatientSerializers(created, many=True)
#     return Response(ser.data)


# # PATION FILTER
# @api_view(['GET'])
# def filter_pation_by_month(request):
#     current_datetime = datetime.now()
#     a = current_datetime.strftime("%m")
#     patient = Patient.objects.all()
#     monthly_patient = []
#     for i in patient:
#         b = str(i.created_at)[5:7]
#         if  int(b)== int(a):
#             monthly_patient.append(i)
#     ser = PatientSerializers(monthly_patient, many=True)
#     return Response (ser.data)
#
#
# # @api_view(['GET'])
# # def filter_pation_by_day(request):
# #     current_datetime = datetime.now()
# #     g = current_datetime.strftime("%d")
# #     pation = Patient.objects.all()
# #     dayly_patient = []
# #     for i in pation :
# #         r = (i.created_at)[7:10]
# #         if int(r) == int(g):
# #             dayly_patient.append(i)
# #     ser = PatientSerializers(dayly_patient, many=True)
# #     return Response(ser.data)
#
#
# @api_view(['GET'])
# def filter_report_by_month(request):
#     current_datetime = datetime.now()
#     a = current_datetime.strftime("%m")
#     patient = Patient.objects.all()
#     monthly_patient = []
#     for i in patient:
#         b = str(i.created_at)[5:7]
#         if  int(b)== int(a):
#             monthly_patient.append(i)
#     ser = PatientSerializers(monthly_patient, many=True)
#     return Response(ser.data)


@api_view(['GET'])
def all_employee(request):
    employee = Employee.objects.all()
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_name(request):
    name = request.GET.get('name')
    employee = Employee.objects.filter(name=name)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emploee_by_expertise(request):
    specialty = request.GET.get('specialty')
    employee = Employee.objects.filter(specialty=specialty)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emploee_by_status(request):
    status_employee = request.GET.get('status_employee')
    employee = Employee.objects.filter(status_employee=status_employee)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emploee_by_room(request):
    private_room = request.GET.get('private_room')
    employee = Employee.objects.filter(private_room=private_room)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)#IShlamadi


@api_view(['GET'])
def filter_amploee_by_time(request):
    time = request.GET.get('time')
    employee = Employee.objects.filter(time = time)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_section(request):
    section = request.GET.get('section')
    employee = Employee.objects.filter(section=section)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def all_section(request):
    emploee = Section.objects.all()
    ser = SectionSerializers(emploee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def all_class(request):
    room = Room.objects.all()
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_capacity(request):
    capacity = request.GET.get('capacity')
    room = Room.objects.filter(capacity=capacity)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_gender(request):
    status_gender = request.GET.get('status_gender')
    room = Room.objects.filter(status_gender=status_gender)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)
