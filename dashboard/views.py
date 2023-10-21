from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from main.serializers import *
from main.models import *
# Create your views here.


# CRUD EMPLOEE
class CreateEmploye(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class UpdateEmploye(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class DeleteEmploye(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
# END CRUD EMPLOEE

# CRUD SECTION
class CreateSection(CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class UpdateSection(UpdateEmploye):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class DeleteSection(DestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers

# End SECTION

# CRUD ROOM
class CreateRoom(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class UpdateRoom(UpdateEmploye):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
# End SECTION

# CRUD PATIENT
class CreatePatient(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


class UpdatePatient(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
# END CRUD PATIENT

# CRUD OPERATION
class CreateOperation(CreatePatient):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class UpdateOperation(UpdateEmploye):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class DeleteOperation(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers
# END CRUD OPERATION

# CRUD Info
class CreateInformation(CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers


class UpdateInfprmation(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers


class DeleteInformation(DestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers
# END CRUD Info

# CRUD CASSA
class CreateCassa(CreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


class UpdateCassa(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


class DeleteCassa(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers
#END CRUD CASSA

# CRUD Report
class CreateReport(CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


class UpdateReport(UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


class DeleteReport(DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
# END CRUD Report

# CRUD Queue
class CreateQueue(CreateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializers


class UpdateQueue(UpdateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializers


class DeleteQueue(DestroyAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializers
#END CRUD Queue

# CRUD Attendance
class CreateAttendance(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class UpdateAttendance(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class DeleteAttendance(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers
#END CRUD Attendance
# CRUD Payment
class CreatePayment(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class UpdatePayment(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class DeletePayment(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers
#END CRUD Payment