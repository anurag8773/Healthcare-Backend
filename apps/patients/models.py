from django.db import models
from django.conf import settings

class Patient(models.Model):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
