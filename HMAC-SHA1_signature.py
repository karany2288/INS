#  ========================================================================================================================
# ||---------------Aim: Write a program to calculate HMAC-SHA1 Signature--------------------------------------------------||
#  ========================================================================================================================

import hashlib
str= input("Enter the value to encode: ")
result= hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is: ")
print(result.hexdigest())