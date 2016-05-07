from rest_framework import serializers
from common.serializer import ContactSerializer
from organizations.models import Organization, OrganizationContact


class OrganizationSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    location_name = serializers.ReadOnlyField()
    industry_name = serializers.ReadOnlyField()

    class Meta:
        model = Organization
        
        
class OrganizationContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrganizationContact