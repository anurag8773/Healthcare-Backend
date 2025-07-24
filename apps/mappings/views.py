from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorSerializer

class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
     # Override retrieve to return all doctors for a patient
    def retrieve(self, request, pk=None):
        """
        GET /api/mappings/<patient_id>/ 
        Returns all doctors assigned to the given patient_id
        """
        # Get all doctor IDs mapped to this patient
        doctor_ids = PatientDoctorMapping.objects.filter(patient_id=pk).values_list('doctor_id', flat=True)
        doctors = Doctor.objects.filter(id__in=doctor_ids)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
