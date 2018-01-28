import re


def user_info_validate_data(data):
    """ validate the user registration form data """
    if "password" not in data or len(data["password"]) < 6:
        return "Password should be in minimum 6 length"
    if data["password"] != data["re_password"]:
        return "Enter password and re password has not matched"
    if "first_name" not in data or len(data["first_name"]) < 1:
        return "Enter first name is not correct"
    if "phone_no" in data:
        if len(data["phone_no"]) < 10:
            return "phone number should be in minimum 10 length"
    if "email" in data:
        email = str(data["email"]).lower()
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match is None:
            return "Enter email id is not valid"
    return "success"


def save_user_auth_key(session, user_id, auth_key):
    """ save user_id and auth_key in current session after login """
    session['auth_key'] = str(auth_key)
    session['user_id'] = str(user_id)




