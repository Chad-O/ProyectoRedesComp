
import hashlib

str= "OTORRINOLARINGOLOGIA"


result = hashlib.sha256(str.encode())
# Imprime el resultado en Hexadecimal:
print("SHA256: ")
print(result.hexdigest())





