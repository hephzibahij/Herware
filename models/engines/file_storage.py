import os
from typing import Union
from datetime import datetime, timedelta
from .base_model import BaseModel
from .data import Data
from .user import User


class FileStorage:
    """
    File Storage Class for the Herware project
    """
    @staticmethod
def save_user_data(user: User, data: Union[dict, BaseModel], file_path: str):
    """
    Save user and device data to a file
    :param user: User model instance
    :param data: Data model instance or dictionary of data
    :param file_path: Path to the file where data needs to be saved
    """


# Convert data to Data model instance if it's a dictionary
if isinstance(data, dict):
    data = Data(data=json.dumps(data), user=user)

    # Write data to file
with open(file_path, 'w') as file:
    file.write(json.dumps(data.__dict__))


@staticmethod
def fetch_user_data(user: User, file_path: str) -> Union[Data, dict]:
    """
    Fetch user and device data from a file
    :param user: User model instance
    :param file_path: Path to the file where data needs to be fetched
    :return: Data model instance or dictionary of data
    """


# Read data from file
with open(file_path, 'r') as file:
    fetched_data = json.loads(file.read())

    # Convert fetched data to Data model instance
fetched_data = Data(data=fetched_data, user=user)

# Convert the fetched data to a dictionary
return fetched_data.__dict__ if isinstance(
    fetched_data, Data) else fetched_data


@staticmethod
def delete_user_data(user: User, file_path: str):
    """
    Delete user and device data from the file
    :param user: User model instance
    :param file_path: Path to the file where data needs to be deleted
    """


# Delete file
os.remove(file_path)
