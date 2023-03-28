from cryptographyFramework import *

initializeWrite()
user = "vini"
password = "1202"
encryptedText = encryptMessage(user, password, "É a tatto da aranhaa!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Bah mt spider cpx!")
saveNewLine(encryptedText)

