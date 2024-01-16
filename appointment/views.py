from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset=models.Appointment.objects.all()
    serializer_class=serializers.AppointmentSerializer

    # custom query 
    def get_queryset(self):
        queryset=super().get_queryset() #7 no line ba parent k niye ashlam 
        patient_id=self.request.query_params.get('patient_id')

        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset
    # doctor 
    def get_queryset(self):
        queryset=super().get_queryset() #7 no line ba parent k niye ashlam 
        doctor_id=self.request.query_params.get('doctor_id')

        if doctor_id:
            queryset=queryset.filter(doctor_id=doctor_id)
        return queryset