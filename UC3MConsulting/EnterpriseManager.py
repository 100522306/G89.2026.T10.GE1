import json
from .EnterpriseManagementException import EnterpriseManagementException
from .EnterpriseRequest import EnterpriseRequest

class EnterpriseManager:
    control_character_group1 = ["A", "B", "E", "H"]
    control_character_group2 = ["K", "P", "Q", "S"]
    group2_index = {
        0: "J",
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I"
    }

    def __init__(self):
        pass

    def validate_cif(self, cif):

        # Basic format check: 9 characters
        if not cif or len(cif) != 9:
            return False

        # Extract the central numeric block (7 digits)
        digits_string = cif[1:8]
        letter = cif[0]
        control_character = cif[8]

        # Cast the digit string to integers
        try:
            digits_block = list(map(int, digits_string))
        except Exception as e:
            raise EnterpriseManagementException("Invalid CIF - String Decoding Error") from e


        # ALGORITHM IMPLEMENTATION
        sum_even = 0
        sum_odd = 0

        for i in range(7):
            digit = digits_block[i]

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

        return self.is_correct_control_character(letter, base_digit, control_character)

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

    def is_correct_control_character(self, letter, base_digit, control_character) -> bool:
        if letter in self.control_character_group1:
            try:
                control_number = int(control_character)
            except ValueError as e:
                raise EnterpriseManagementException("Invalid CIF - Invalid Control Character") from e
            return control_number == base_digit

        elif letter in self.control_character_group2:
            try:
                expected_control_character = self.group2_index.get(base_digit)
            except KeyError as e:
                raise EnterpriseManagementException("Invalid CIF - Control Character Not Found") from e
            return control_character == expected_control_character

        raise EnterpriseManagementException("Invalid CIF - Letter Not Found")