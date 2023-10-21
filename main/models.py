from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
class User(AbstractUser):
    phone  = models.CharField(max_length=13, unique=True, blank=False, validators=[
    RegexValidator(
        regex='^[\+]9{2}8{1}[0-9]{9}$',
        message='Invalid phone number',
        code='invalid_number'
    ),])
    adress = models.CharField(max_length=50,verbose_name="manzil")

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Employee(models.Model):
    name = models.CharField(max_length=25, verbose_name='Ismi :')
    phone = models.CharField(max_length=13, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    describtion = models.CharField(max_length=250, verbose_name='Hodimning tasnifi :', null=True, blank=True)
    private_room = models.ForeignKey(to='Private_room', on_delete=models.SET_NULL, verbose_name='Hodimning honasi :', null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    start_time = models.TimeField(verbose_name='Hodimning ish boshlash vaqti :')
    end_time = models.TimeField(verbose_name='Hodimning ish vaqtining tugashi :')
    specialty = models.CharField(max_length=250, verbose_name='Hodimning mutaxassisligi', null=True, blank=True)
    status_employee = models.IntegerField(blank=False, verbose_name='Ishchilar statusi :', choices=
    (
        (1, "Doctor"),
        (2, "Admin"),
        (3, "Work manager")
    ))
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

    def __str__(self):
        return self.name


class Private_room(models.Model):
    room_name = models.CharField(max_length=50, verbose_name='Hodim honasining nomi (Masalan: Kardiologiya) :')
    room_number = models.IntegerField(verbose_name='Hodim honasining raqami :')
    class Meta:
        verbose_name = "Private_room"
        verbose_name_plural = 'Private_room'

    def __str__(self):
        return self.room_name


class Patient(models.Model):
    name = models.CharField(max_length=25)
    doctor = models.ForeignKey(to=Employee, on_delete=models.CASCADE, verbose_name='Bemorning doctori :')
    photo = models.ImageField(upload_to='patient/', verbose_name='Bemorning rasmi :', null=True, blank=True)
    phone = models.CharField(max_length=13, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    created_at = models.DateTimeField(verbose_name='Bemor honasining yaratilgan vaqti :')
    diagnos = models.CharField(max_length=100, verbose_name='Tashxisi :')
    day = models.IntegerField(verbose_name='Bemorning honadagi kuni :')
    status_gender = models.IntegerField(blank=False, verbose_name='Bemorning jinsi :', choices=
    (
        (1, 'Famele'),
        (2, 'Male'),
    ))

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = 'Patient'

    def __str__(self):
        return self.id


class Section(models.Model):
    name = models.CharField(max_length=25, verbose_name='Bo`limi :')

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = 'Section'

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=25, verbose_name='Honaning nomi :')
    is_free = models.BooleanField(default=True, verbose_name='Hona bo`sh / band :')
    capacity = models.IntegerField(default=0, verbose_name='Honaning sig`imi :')
    price = models.IntegerField(verbose_name='Hona narxi :')
    section = models.ForeignKey(to=Section, on_delete=models.SET_NULL, verbose_name='Bo`limi :', null=True)
    status = models.IntegerField(blank=False, verbose_name='Hona statusi :', choices=
    (
        (1, "Patient"),
        (2, "Employee")
    ))
    category = models.IntegerField(blank=False, verbose_name='Hona bo`limi :', choices=
    (
        (1, "Lux"),
        (2, "Econom"),
        (3, "Operatsiya")
    ))

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = 'Room'

    def __str__(self):
        return self.name

class Operation(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.PROTECT, verbose_name='Bemor :')
    doctor = models.ManyToManyField(to=Employee, verbose_name='Bemorni operatsiya qiluvchi doctor :')
    durationtime = models.TimeField(verbose_name='Operatsiya davomiyligi :')
    time = models.DateTimeField(verbose_name='Operatsiya vaqti :')
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, verbose_name='Opertsiya honasini belgilang :')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Operation"
        verbose_name_plural = 'Operation'

    def __str__(self):
        return self.patient


class Info(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nomi :")
    about = models.TextField(verbose_name='Klinika haqida :')
    employee_number = models.IntegerField(default=0, verbose_name='Ishchilar soni :')
    patient_number_healing = models.IntegerField(verbose_name='Shifo topganlar soni :')

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = 'Info'

    def __str__(self):
        return self.name


class Cassa(models.Model):
    password = models.CharField(max_length=8, verbose_name='Kassa parolini kiriting :')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Casssa balanci :')

    class Meta:
        verbose_name = "Cassa"
        verbose_name_plural = 'Cassa'


class Report(models.Model):
    income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kiruvchi mablag` :')
    expence = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Chiquvchi mablag` :')
    description = models.CharField(max_length=255, verbose_name='Hisobot :')
    date = models.DateField(auto_now=True, verbose_name='Sanasi :')

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = 'Report'




class Queue(models.Model):
    doctor = models.ManyToManyField(to=Employee)
    number = models.IntegerField(default=0, verbose_name='Navbat soni :')
    description = models.CharField(max_length=255, verbose_name='Tasnifi :')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Navbat yaratilishi :')

    class Meta:
        verbose_name = "Queue"
        verbose_name_plural = 'Queue'

    def __str__(self):
        return self.doctor


class Attendance(models.Model):
    doctor = models.ForeignKey(to=Employee, on_delete=models.PROTECT, verbose_name='Doctorning ismi :')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = 'Attendance'

    def __str__(self):
        return self.doctor

class Payment(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, verbose_name='Bemor :')
    total = models.IntegerField(verbose_name='Summa :')
    description = models.TextField(null=True, verbose_name='Tasnifi :')
    created = models.DateTimeField(auto_created=True, verbose_name='Yaratilgan :')
    cod = models.CharField(max_length=25, unique=True, verbose_name='Code :')

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = 'Payment'

    def __str__(self):
        return self.patient