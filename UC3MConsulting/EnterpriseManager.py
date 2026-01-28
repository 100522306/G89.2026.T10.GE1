import json
from .EnterpriseManagementException import EnterpriseManagementException
from .EnterpriseRequest import EnterpriseRequest

class EnterpriseManager:
    def __init__(self):
        pass

    def ValidateCIF( self, CiF ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise EnterpriseManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            T_CIF = DATA["cif"]
            T_PHONE = DATA["phone"]
            E_NAME = DATA["enterprise_name"]
            req = EnterpriseRequest(T_CIF, T_PHONE,E_NAME)
        except KeyError as e:
            raise EnterpriseManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateCIF(T_CIF) :
            raise EnterpriseManagementException("Invalid FROM IBAN")
        return req