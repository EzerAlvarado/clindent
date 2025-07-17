from django.shortcuts import render

# Create your views here.
#models
from clinica.models import Claim
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.claims import ClaimModelSerializer
#filters
from clinica.filters.claims import ClaimFilter

class ClaimViewSet(viewsets.ModelViewSet):
    """
    View de Claims
    Maneja CRUD
    """
    queryset=Claim.objects.all()
    serializer_class = ClaimModelSerializer
    filterset_class = ClaimFilter