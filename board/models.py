from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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

    


