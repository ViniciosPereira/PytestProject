from cryptographyFramework import *

initializeRead()
user = "Tales"
password = "T@les123456!"
line1 = readNextLine()
print(line1)
print(decryptMessage(user, password, line1))
line2 = readNextLine()
print(line2)
print(decryptMessage(user, password, line2))