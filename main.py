from UC3MConsulting import EnterpriseManager
import string

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3


def Encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) + shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def Decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) - shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded


def main():

    mng = EnterpriseManager()
    res = mng.ReadproductcodefromJSON("test.json")
    strRes = res.__str__()
    print(strRes)
    EncodeRes = Encode(strRes)
    print("Encoded Res "+ EncodeRes)
    DecodeRes = Decode(EncodeRes)
    print("Decoded Res: " + DecodeRes)
    print("cif: " + res.ENTERPRISE_CIF)
    print("enterprise_name: " + res.ENTerprise_Name)
    print("enterprise_phone: " + res.PHONE_NUMBER)

if __name__ == "__main__":
    main()
