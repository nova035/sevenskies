from common.models import Location, Industry, ContactType, Contact

from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType


class ContactSerializer(serializers.ModelSerializer):
    contact_type_name = serializers.ReadOnlyField()

    class Meta:
        model = Contact