import json
from datetime import datetime

class EnterpriseRequest:
    def __init__(self, cif, phone, name):
        self.__name = name
        self.__cif = cif
        self.__phone = phone
        just_now = datetime.now()
        self.__time_stamp = datetime.timestamp(just_now)

    def __str__(self):
        return "Enterprise:" + json.dumps(self.__dict__)

    @property
    def enterprise_cif(self):
        return self.__cif

    @enterprise_cif.setter
    def enterprise_cif(self, value):
        self.__cif = value

    @property
    def phone_number(self):
        return self.__phone

    @phone_number.setter
    def phone_number(self, value):
        self.__phone = value

    @property
    def enterprise_name(self):
        return self.__name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self.__name = value

    # ADDED THIS to fix the 'unused-private-member' error
    @property
    def timestamp(self):
        return self.__time_stamp