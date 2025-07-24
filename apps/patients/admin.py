from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'created_by', 'created_at')
    search_fields = ('name', 'age')
    list_filter = ('created_by',)
