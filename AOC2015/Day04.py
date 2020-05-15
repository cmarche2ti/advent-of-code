import hashlib
import re

code = "ckczppom"

count = 0
p = True


def hex_encode(s):
    text = hashlib.md5(s.encode())
    return text.hexdigest()


while p:
    value = code + str(count)
    # finds hex with 5 zeros
    # if re.findall("^0{5}", hex_encode(value)):
    # finds hex with 6 zeros
    if re.findall("^0{6}", hex_encode(value)):
        print("Found it")
        p = False
    print(count)
    count += 1
    print(hex_encode(value))
