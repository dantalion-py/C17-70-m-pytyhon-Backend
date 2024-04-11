from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
    )

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    speciality = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.speciality}"
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    medical_history = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.get_full_name()}"

class Administrator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.first_name()
