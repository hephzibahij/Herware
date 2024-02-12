from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Abstract base model for the Herware project
    """


created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('Created at'))
updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))


class Meta:
    abstract = True


def __str__(self):
    return f"BaseModel - ID: {self.id},
    Created At: {self.created_at}, Updated At: {self.updated_at}"


class User(AbstractUser):
    """
    User model for the Herware project
    """


name = models.CharField(max_length=100, blank=True, null=True)
organization = models.CharField(max_length=100, blank=True, null=True)
address = models.CharField(max_length=255, blank=True, null=True)
user_role = models.CharField(
    max_length=50, choices=[
        ('admin', 'Administrator'), ('user', 'User'), ('guest', 'Guest')])
time_zone = models.CharField(max_length=100, blank=True, null=True)
language = models.CharField(max_length=50, blank=True, null=True)
phone_number = models.CharField(max_length=15, blank=True, null=True)
alternative_email = models.EmailField(blank=True, null=True)
date_of_birth = models.DateField(blank=True, null=True)
security_question1 = models.CharField(max_length=50, blank=True, null=True)
security_answer1 = models.CharField(max_length=50, blank=True, null=True)
security_question2 = models.CharField(max_length=50, blank=True, null=True)
security_answer2 = models.CharField(max_length=50, blank=True, null=True)
terms_of_service_accepted = models.BooleanField(default=False)
privacy_policy_accepted = models.BooleanField(default=False)


def __str__(self):
    return self.username


class Device(models.Model):
    """
    Device model for the Herware project
    """


user = models.ForeignKey(User, on_delete=models.CASCADE)
name = models.CharField(max_length=100)
device_type = models.CharField(max_length=50)
device_id = models.CharField(max_length=50)
configuration_settings = models.JSONField(default=dict)


def __str__(self):
    return self.name


class Data(models.Model):
    """
    Data model for the Herware project
    """


user = models.ForeignKey(User, on_delete=models.CASCADE)
device = models.ForeignKey(Device, on_delete=models.CASCADE)
data_type = models.CharField(max_length=50)
value = models.TextField()
submission_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"Data Submission by {self.user.username} -


{self.device.name} - {self.data_type}"
