import json
from datetime import datetime


class EnterpriseRequest:
    def __init__(self, Cif,phOnE, ENAME):
        self.__EnterpriseNAME = ENAME
        self.__cIF = Cif
        self.__pHONe = phOnE
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "Enterprise:" + json.dumps(self.__dict__)

    @property
    def ENTERPRISE_CIF(self):
        return self.__cIF
    @ENTERPRISE_CIF.setter
    def ENTERPRISE_CIF(self, value):
        self.__cIF = value

    @property
    def PHONE_NUMBER(self):
        return self.__pHONe
    @PHONE_NUMBER.setter
    def PHONE_NUMBER(self, value):
        self.__pHONe = value

    @property
    def ENTerprise_Name(self):
        return self.__EnterpriseNAME
    @ENTerprise_Name.setter
    def ENTerprise_Name(self, value):
        self.__EnterpriseNAME = value