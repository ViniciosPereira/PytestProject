import re
def validate_username(username):
    if len(username) > 30:
        return False
    if not re.match(r'^[A-Za-z0-9][A-Za-z0-9]*$', username):
        return False
    if not username[0].isupper():
        return False
    return True

def validate_password(password):
    special_chars = ['$', '@', '#', '%', '&', '*', '_', '-', '+', '=','!']
    if len(password) < 10:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in special_chars for char in password):
        return False
    return True

def validate_text(message):
    if len(message) >= 70:
        return False


    