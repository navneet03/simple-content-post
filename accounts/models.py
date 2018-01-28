from __future__ import unicode_literals
import uuid
from django.db import models


class User(models.Model):
    """
    Model that represents an user.
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=128,  null=True)
    phone_number = models.CharField(blank=True, max_length=20, null=True)

    gender_type_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, null=True, blank=True, choices=gender_type_CHOICES)

    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.

        :return: string
        """
        return "{0} {1}".format(self.first_name, self.last_name)

