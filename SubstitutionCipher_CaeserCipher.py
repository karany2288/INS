#  ==================================================================================================================
# ||---------------Aim:Write a program to implement the substitution cipher technique: Caeser Cipher.---------------||
#  ==================================================================================================================

def encrypt(text,s):
    result = " "
    for i in range(len(text)):
        char= text[i]
        
        if (char.isupper()):
            result += chr((ord(char)+5-65)%26+65)
        else:
            result += chr((ord(char)+5-9)%26+97)
    return result
text = input("Enter the Text to encrypt: ")
s=3
print("Text: "+ text)
print("Cipher: "+ encrypt(text,s))