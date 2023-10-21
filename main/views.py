from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from datetime import datetime, timedelta

@api_view(['GET'])
def get_date_patient(request):
    created_at = request.GET.get('created_at')
    created = Patient.objects.filter(created_at=created_at)
    ser = PatientSerializers(created, many=True)
    return Response(ser.data)


# PATION FILTER
@api_view(['GET'])
def filter_pation_by_month(request):
    current_datetime = datetime.now()
    a = current_datetime.strftime("%m")
    patient = Patient.objects.all()
    monthly_patient = []
    for i in patient:
        b = str(i.created_at)[5:7]
        if  int(b)== int(a):
            monthly_patient.append(i)
    ser = PatientSerializers(monthly_patient, many=True)
    return Response (ser.data)


@api_view(['GET'])
def filter_pation_by_year(request):
    date = request.GET.get('date')
    patient = Patient.objects.all()
    monthly_patient = []
    for i in patient:
        b = str(i.created_at)[0:5]
        if date == b:
            monthly_patient.append(i)
    ser = PatientSerializers(monthly_patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_pation_by_day(request):
    date = request.GET.get('date')
    patient = Patient.objects.all()
    yearly_patient = []
    for i in patient:
        a = str(i.created_at)[8:11]
        if date == a:
            yearly_patient.append(i)
    ser = PatientSerializers(yearly_patient, many=True)
    return Response(ser.data)

#END PATION FILTER

# REPORT FILTER
@api_view(['GET'])
def filter_report_by_day(request):
    date = request.GET.get('date')
    report = Report.objects.all()
    dayly_report = []
    for i in report:
        a = str(i.date)[8:1]
        if date == i:
            dayly_report.append(i)