# models/device.py
from django.db import models
from django.conf import settings
from .base_model import BaseModel
from .user import User


class Device(BaseModel):
    """
    Device model for the Herware project
    """


user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='devices',
    verbose_name='User')
name = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    help_text='Name of the device')
device_type = models.CharField(max_length=50, blank=True, null=True, choices=[
    ('smartphone', 'Smartphone'),
    ('tablet', 'Tablet'),
    ('laptop', 'Laptop'),
    ('desktop', 'Desktop'),
    ('iot_device', 'IoT Device'),
], help_text='Type of the device')
device_id = models.CharField(
    max_length=50,
    blank=True,
    null=True,
    help_text='Unique identifier for the device')
configuration_settings = models.JSONField(
    default=dict,
    blank=True,
    null=True,
    help_text='Device configuration settings')
registered_at = models.DateTimeField(
    auto_now_add=True,
    blank=True,
    null=True,
    verbose_name='Registered at')
last_synced_at = models.DateTimeField(
    auto_now=True,
    blank=True,
    null=True,
    verbose_name='Last synced at')
status = models.CharField(max_length=50, blank=True, null=True, choices=[
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('pending', 'Pending'),
    ('removed', 'Removed'),
], help_text='Status of the device')


def __str__(self):
    return self.name
