def check_password_strength(password):
    '''
    Program to check the strength of the input password.
    Parameters:
    password (str): Input password.

    Returns:
    str: "Weak", "Strong", or "Average" based on password strength.
    '''
    special_chars = list('@#$%&*')
    
    
    isdigit_there = any(char.isdigit() for char in password)
    isupper_there = any(char.isupper() for char in password)
    isspchar_there = any(char in special_chars for char in password)
    check_lower = any(char.islower() for char in password)

    all_true = all([isdigit_there, isupper_there, isspchar_there, check_lower])

    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and all_true:
        return "Strong"
    else:
        return "Average"
    

input_password = input("Create Password:")
strength = check_password_strength(input_password)
print(f"\nYour password is {strength}!")