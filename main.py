from UC3MConsulting.EnterpriseManager import EnterpriseManager
from UC3MConsulting.EnterpriseManagementException import EnterpriseManagementException


def test_file(manager, file_path):
    print(f"--- Testing file: {file_path} ---")
    try:
        req = manager.read_product_code_from_json(file_path)
        print(f"SUCCESS: CIF {req.ENTERPRISE_CIF} is valid.")
        print(f"Enterprise: {req.ENTerprise_Name}")
    except EnterpriseManagementException as e:
        print(f"VALIDATION ERROR: {e.message}")
    print("-" * 30)


def main():
    mng = EnterpriseManager()

    # Example 1: Valid CIF [cite: 96]
    test_file(mng, "test.json")

    # Example 2: Non-valid CIF [cite: 96]
    test_file(mng, "test_wrong.json")


if __name__ == "__main__":
    main()