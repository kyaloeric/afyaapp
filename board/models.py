from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField()
    registration_date = models.DateTimeField("date reistered")


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    registration_date = models.DateTimeField("date registered")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    waiting_status = models.BooleanField()

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

    


# Appointment
class Appointment(models.Model):  # customer appointment details
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="CustomerApp")  # customer fk
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="EngineerApp")  # engineer fk
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="CustomerApprovedApp")  # customer fk
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="EngineerApprovedApp")  # engineer fk
    approval_date = models.DateField()  # date appointment approved
    description = models.TextField()  # appointment description
    completed_date = models.DateField(null=True, blank=True)  # date of completed appointment

    def __str__(self):
        return f'{self.customer} Approved Appointment Information'