from rest_framework import serializers

from .models import Donors

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = '__all__'

