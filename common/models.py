from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models


LOCATION_TYPES = (
    ('Town', 'Town'),
    ('County', 'County')
)


class ContactType(models.Model):
    name = models.CharField(
        max_length=100, unique=True,
        help_text="A short name, preferably 6 characters long, "
        "representing a certain type of contact e.g EMAIL")
    description = models.TextField(
        null=True, blank=True,
        help_text='A brief description of the contact type.')

    def __str__(self):
        return self.name


class Contact(models.Model):
    contact = models.CharField(
        max_length=100,
        help_text="The actual contact of the person e.g test@mail.com,"
        " 07XXYYYZZZ")
    contact_type = models.ForeignKey(
        ContactType,
        help_text="The type of contact that the given contact is e.g email"
        " or phone number",
        on_delete=models.PROTECT)

    def __str__(self):
        return "{}: {}".format(self.contact_type.name, self.contact)

    class Meta(object):
        unique_together = ('contact', 'contact_type')

    @property
    def contact_type_name(self):
        return self.contact_type.name


class UserContact(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_contacts', on_delete=models.PROTECT)
    contact = models.ForeignKey(Contact)

    def __str__(self):
        return "{}: ({})".format(self.user, self.contact)

    def validate_user_linked_to_a_certain_contact_once(self):
        """
        Ensures that user contacts are not duplicated
        """
        user_contact_instance_count = self.__class__.objects.filter(
            user=self.user, contact=self.contact).count()
        if user_contact_instance_count > 0 and not self.deleted:
            msg = "The user contact {0} is already added to the user".format(
                self.contact.contact)
            raise ValidationError(
                {
                    "contact": [msg]

                })

    def clean(self, *args, **kwargs):
        super(UserContact, self).clean(*args, **kwargs)
        self.validate_user_linked_to_a_certain_contact_once()


class Location(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=LOCATION_TYPES, default='Town')

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


