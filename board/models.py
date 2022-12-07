from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
# Default user - deleted
def default_user():  # deleted users
    user = User(username="deleteduser", email="deleteduser@deleted.com")
    return user.id


# Admin
class Admin(models.Model):  # Admin details
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")  # user foreign key
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    first_name = models.CharField(max_length=100, default='first_name')  # admin first name
    last_name = models.CharField(max_length=100, default='last_name')  # admin lastname
    dob = models.DateField(default=datetime.date.today)  # date of birth
    # contact?
    address = models.CharField(max_length=300, default="address")  # admin address
    city = models.CharField(max_length=100, default="city")  # admin city
    county = models.CharField(max_length=100, default="county")  # admin county
    postcode = models.IntegerField(default=0)  # admin postcode
    status = models.BooleanField(default=False)  # admin status (approved/on-hold)

    def __str__(self):
        return f'{self.admin.username} Admin Profile'


# Doctors 
class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture

    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField()
    registration_date = models.DateTimeField("date reistered")
    city = models.CharField(max_length=100, default="city")  # engineer city
    country = models.CharField(max_length=100, default="country")  # engineer country
    postcode = models.IntegerField(default=0)  # engineer postcode
    status = models.BooleanField(default=False)  # tatus(approved/on-hold)

    def __str__(self):
        return f'{self.engineer.username} Engineer Profile'


# Patients
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    registration_date = models.DateTimeField("date registered")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default="city")  # customer city
    country = models.CharField(max_length=100, default="country")  # customer country
    postcode = models.IntegerField(default=0)  # customer postcode
    status = models.BooleanField(default=False)  # customer status (approved/on-hold)

    def __str__(self):
        return f'{self.patient.username} Patient Profile'


# Appointment
class Appointment(models.Model):  # customer appointment details
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientApp")  # patient fk
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorApp")  # doctor fk
    description = models.TextField(max_length=500)  # appointment description
    app_link = models.TextField(null=True, blank=True)  # video call room link
    app_date = models.DateField(null=True, blank=True)  # call date
    app_time = models.TimeField(null=True, blank=True)  # call time/slot
    status = models.BooleanField(default=False)  # appointment status (approved/on-hold)
    completed = models.BooleanField(default=False)  # appointment completed/to-be-done
    # approval_date = models.DateField(null=True, blank=True)  # date appointment approved
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.description} Appointment Information'



# Appointment rating
class AppointmentRating(models.Model):
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0)])

    def __str__(self):
        return f'{self.rating} Stars - Appointment Rating Information'


# Approved appointment
class ApprovedCustomerAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientApprovedApp")  # Patient fk
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="PatientApprovedApp")  # Doctor fk
    approval_date = models.DateField()  # date appointment approved
    description = models.TextField()  # appointment description
    completed_date = models.DateField(null=True, blank=True)  # date of completed appointment

    def __str__(self):
        return f'{self.patient} Approved Appointment Information'