from __future__ import unicode_literals
import uuid

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.mail.message import EmailMultiAlternatives
from django.core.validators import validate_email, RegexValidator
from django.utils import timezone
from django.template import loader, Context
from django.conf import settings
from django.db import models


def send_email_on_signup(user, user_password):
    html_email_template = loader.get_template(
        "registration/registration_success.html")
    context = Context(
        {
            "user": user,
            "user_password": user_password,
            "login_url": settings.FRONTEND_URL
        }
    )
    plain_text = loader.get_template("registration/registration_success.txt")
    subject = "Account Created"
    plain_text_content = plain_text.render(context)
    html_content = html_email_template.render(context)
    mfl_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(
        subject, plain_text_content, mfl_email, [user.email])
    msg.attach_alternative(html_content, "text/html")
    # msg.send()


def check_password_strength(raw_password):
    if (len(raw_password) >= 8 and not raw_password.isalpha() and not
    raw_password.isdigit()):
        return True
    else:
        error = (
            {
                "password": [
                    "The password must be at least 8 characters and contain both letters and numbers"  # noqa
                ]
            }
        )
        raise ValidationError(error)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, is_staff=False, **extra_fields):
        check_password_strength(password)
        now = timezone.now()
        validate_email(email)
        p = make_password(password)
        email = CustomUserManager.normalize_email(email)
        user = self.model(email=email, first_name=first_name, password=p,
                          is_staff=is_staff, is_active=True, date_joined=now, **extra_fields)
        user.save(using=self._db)
        send_email_on_signup(user, password)
        return user

    def create_superuser(self, email, first_name, password, is_staff=True, **extra_fields):
        user = self.create_user(email, first_name, password, **extra_fields)
        user.is_staff = is_staff
        user.is_active = True
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return super(
            CustomUserManager, self).get_queryset().filter(deleted=False)


class JobTitle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100, unique=True,
        help_text="A short name for the job title")
    abbreviation = models.CharField(
        max_length=100, null=True, blank=True,
        help_text="The short name for the title")
    description = models.TextField(
        null=True, blank=True,
        help_text="A short summary of the job title")
    search = models.TextField(
        null=True, blank=True,
        help_text='A dummy field to enable search on the model through a'
                  ' filter')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ('-created', )
        permissions = (
            (
                "view_jobtitle",
                "Can view job title"
            ),
        )


class CustomUser(AbstractBaseUser):
    email = models.EmailField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=60, null=False, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    other_names = models.CharField(max_length=80, null=False, blank=True,
                                   default="")
    job_title = models.ForeignKey(JobTitle, null=True, blank=True, help_text="The job title of the user",
                                  on_delete=models.PROTECT)
    username = models.CharField(max_length=60, null=True, blank=True, unique=True, validators=[
        RegexValidator(regex=r'^\w+$', message='Preferred name contain only letters numbers or underscores')
    ])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    search = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        'self', null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey(
        'self', null=True, blank=True, related_name='+')
    updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
    everything = BaseUserManager()

    def set_password(self, raw_password):
        """Overridden so that we can keep track of password age"""
        super(CustomUser, self).set_password(raw_password)

    def __str__(self):
        return self.get_full_name

    @property
    def get_short_name(self):
        return self.first_name

    @property
    def get_full_name(self):
        names = [self.first_name, self.last_name, self.other_names]
        return " ".join([i for i in names if i])

    @property
    def permissions(self):
        return self.get_all_permissions()

    @property
    def contacts(self):
        from common.models import UserContact

        return [
            {
                "id": user_contact.id,
                "contact": user_contact.contact.id,
                "contact_text": user_contact.contact.contact,
                "contact_type": user_contact.contact.contact_type.id,
                "contact_type_name": user_contact.contact.contact_type.name

            } for user_contact in UserContact.objects.filter(user=self)
        ]

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', )
        ordering = ('-date_joined', )

