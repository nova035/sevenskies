import logging

from django.db import transaction
from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from common.models import UserContact, Contact

from .models import CustomUser


LOGGER = logging.getLogger(__name__)


class CustomUserSerializer(serializers.ModelSerializer):
    """This should allow everything about users to be managed"""

    short_name = serializers.ReadOnlyField(source='get_short_name')
    full_name = serializers.ReadOnlyField(source='get_full_name')
    requires_password_change = serializers.ReadOnlyField()
    contacts = serializers.ReadOnlyField()
    job_title_name = serializers.ReadOnlyField(source='job_title.name')

    def _upadate_validated_data_with_audit_fields(
            self, validated_data, is_creation=False):
        if is_creation:
            validated_data['created_by'] = self.context['request'].user
            validated_data['created'] = timezone.now()
        validated_data['updated_by'] = self.context['request'].user
        validated_data['updated'] = timezone.now()
        return validated_data

    def _assign_is_staff(self, user_groups):
        for group in user_groups:
            if group.is_administrator:
                return True
        return False

    def _update_or_create_contacts(self, instance, contacts):
        for contact in contacts:
            if 'id' in contact:
                try:
                    user_contact_obj = UserContact.objects.get(
                        id=contact.get('id'))
                    user_contact_obj.contact.contact = contact.get(
                        'contact_text')
                    user_contact_obj.contact.contact_type_id = contact.get(
                        'contact_type')
                    user_contact_obj.contact.save()
                except UserContact.DoesNotExist:
                    msg = "User contact with id {0} does not exist".format(
                        contact.get('id'))
                    raise ValidationError(
                        {
                            "user_contact": [msg]
                        })
            else:
                contact['updated_by_id'] = self.context.get(
                    'request').user.id
                contact['created_by_id'] = self.context.get(
                    'request').user.id
                contact['contact_type_id'] = contact.pop('contact_type')
                contact['contact'] = contact.pop('contact_text')
                contact_obj = Contact.objects.create(**contact)
                user_contact = {}
                user_contact['updated_by_id'] = self.context.get(
                    'request').user.id
                user_contact['created_by_id'] = self.context.get(
                    'request').user.id
                user_contact['user_id'] = instance.id
                user_contact['contact_id'] = contact_obj.id
                UserContact.objects.create(**user_contact)

    @transaction.atomic
    def create(self, validated_data):
        validated_data = self._upadate_validated_data_with_audit_fields(
            validated_data, is_creation=True)
        validated_data.pop('contacts', None)
        contacts = self.initial_data.pop('contacts', [])

        new_user = CustomUser.objects.create_user(**validated_data)
        new_user.save()
        self._update_or_create_contacts(new_user, contacts)

        return new_user

    @transaction.atomic
    def update(self, instance, validated_data):
        validated_data = self._upadate_validated_data_with_audit_fields(
            validated_data)
        validated_data.pop('groups', None)

        validated_data.pop('contacts', None)
        contacts = self.initial_data.pop('contacts', [])
        pwd = validated_data.pop('password', None)

        # This does not handle password changes intelligently
        # Use the documented password change endpoints
        # Also: teach your API consumers to always prefer PATCH to PUT
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if pwd is not None:
            instance.set_password(pwd)
        instance.save()

        self._update_or_create_contacts(instance, contacts)

        return instance

    class Meta(object):
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
