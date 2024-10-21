#  =====================================================================================================================
# ||---------------Aim: Implement digital Signature algorithm such as RSA based Signature, and verify the integrity and ||
# ||--------------------authenticity of digitally signed message.                                                       ||
#  ======================================================================================================================

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key= RSA.generate(2048)
private_key = key.export_key()
public_key= key.publickey().export_key()

original_document= b"This is the original document content."
modified_document= b"This is the modified document content."

original_hash= SHA256.new(original_document)
modified_hash= SHA256.new(modified_document)

signature= pkcs1_15.new(RSA.import_key(private_key)).sign(original_hash)

try:
    pkcs1_15.new(RSA.importKey(public_key)).verify(modified_hash, signature)
    print("Signature is valid!!")
except(ValueError, TypeError):
    print("Signature is invalid.")