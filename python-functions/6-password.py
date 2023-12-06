def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_upper and has_lower and has_digit):
        return False

    if ' ' in password:
        return False

    return True