import os
import json
from typing import Union
from datetime import datetime, timedelta
from .base_model import BaseModel
from .data import Data
from .user import User
from .device import Device


class DBStorage:
    """
    Database Storage Class for the Herware project
    """
    @staticmethod
def save_user_data(user: User, data: Union[dict, BaseModel]):
    """
    Save user and device data to the database
    :param user: User model instance
    :param data: Data model instance or dictionary of data
    """


# Convert data to Data model instance if it's a dictionary
if isinstance(data, dict):
    data = Data(data=json.dumps(data), user=user)
    data.save()


@staticmethod
def fetch_user_data(
        user: User, days: Union[int, timedelta] = 7) -> Union[Data, dict]:
    """
    Fetch user and device data from the database
    :param user: User model instance
    :param days: Number of days or a timedelta instance data to fetch
    :return: Data model instance or dictionary of data
    """


# Fetch data within the specified time range
data = Data.objects.filter(user=user, created_at__gte=(datetime.now() - days))

# Convert the fetched data to a dictionary
fetched_data = []
for datum in data:
    fetched_data.append(json.loads(datum.data))
    return fetched_data if len(fetched_data) > 1 else fetched_data[0]


@staticmethod
def delete_user_data(user: User, days: Union[int, timedelta] = 7):
    """
    Delete user and device data from the database
    :param user: User model instance
    :param days: Number of days or a timedelta instance of data to delete
    """


Data.objects.filter(user=user, created_at__lt=(datetime.now() - days)).delete()


@staticmethod
def delete_all_user_data(user: User):
    """
    Delete all user and device data from the database
    :param user: User model instance
    """


Data.objects.filter(user=user).delete()
Device.objects.filter(user=user).delete()
