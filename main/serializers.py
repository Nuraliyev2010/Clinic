from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Employee
        fields = "__all__"


class Private_roomSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Private_room
        fields = "__all__"


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Patient
        fields = "__all__"


class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Section
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Room
        fields = "__all__"


class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Operation
        fields = "__all__"


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Info
        fields = "__all__"


class CassaSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Cassa
        fields = "__all__"


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Report
        fields = "__all__"


class QueueSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Queue
        fields = "__all__"


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Attendance
        fields = "__all__"


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Payment
        fields = "__all__"


