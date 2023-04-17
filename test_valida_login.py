import pytest
# from cryptographyFramework import *

from valida_login import validate_username, validate_password


def test_validate_username():
    assert validate_username("Alice") == True
    assert validate_username("bob") == False
    assert validate_username("Charlie1") == True
    assert validate_username("David_") == False
    assert validate_username("Eve-Smith") == False
    assert validate_username("Tales,Klaus") == False
    assert validate_username("Tales") == True
    assert validate_username("Vinicios") == True
    assert validate_username("FirstnameLastnameFirstnameLastnameF") == False


def test_validate_password():
    assert validate_password("Password1@") == True
    assert validate_password("senhcurta") == False
    assert validate_password("Password1") == False
    assert validate_password("password1@") == False
    assert validate_password("PASSWORD1@") == False
    assert validate_password("Password1$@#%&*_-+=") == True

