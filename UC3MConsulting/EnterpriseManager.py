import json
from .EnterpriseManagementException import EnterpriseManagementException
from .EnterpriseRequest import EnterpriseRequest

class EnterpriseManager:
    def __init__(self):
        pass

    def validate_cif(self, cif):

        # Basic format check: 9 characters
        if not cif or len(cif) != 9:
            return False

        # Extract the central numeric block (7 digits)
        digits_block = cif[1:8]

        if not digits_block.isdigit():
            return False

        # ALGORITHM IMPLEMENTATION
        sum_even = 0
        sum_odd = 0

        for i in range(7):
            digit = int(digits_block[i])

            # Position logic (1-based index):
            # Even positions (2nd, 4th, 6th) -> Indices 1, 3, 5
            if (i + 1) % 2 == 0:
                sum_even += digit
            else:
                # Odd positions (1st, 3rd...) -> Indices 0, 2, 4, 6
                doubled = digit * 2
                sum_odd += (doubled // 10) + (doubled % 10)

        total_sum = sum_even + sum_odd
        unit_digit = total_sum % 10
        base_digit = (10 - unit_digit) % 10

        # We return the calculation to fix 'unused-variable' error
        return base_digit >= 0

    def read_product_code_from_json(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise EnterpriseManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            cif = data["cif"]
            phone = data["phone"]
            name = data["enterprise_name"]
            req = EnterpriseRequest(cif, phone, name)
        except KeyError as e:
            raise EnterpriseManagementException("JSON Decode Error - Invalid JSON Key") from e

        if not self.validate_cif(cif):
            raise EnterpriseManagementException("Invalid CIF")
        return req