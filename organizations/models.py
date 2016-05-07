from django.db import models
from django.utils import timezone
from common.models import Industry, Location, Contact


class Organization(models.Model):
    name = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry)
    location = models.ForeignKey(Location)
    description = models.TextField(default='-')
    created = models.DateTimeField(default=timezone.now, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    logo_url = models.CharField(max_length=255, null=True, blank=True)

    @property
    def industry_name(self):
        return self.industry.name

    @property
    def location_name(self):
        return self.location.name

    @property
    def contacts(self):
        my_contacts = []
        org_contacts = OrganizationContact.objects.filter(organization=self)
        for org_contact in org_contacts:
            my_contacts.append(org_contact.contact)
        return my_contacts


class OrganizationContact(models.Model):
    contact = models.ForeignKey(Contact)
    organization = models.ForeignKey(Organization, related_name="org_contacts")