from accounts.models import *
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from accounts.shortcut_func import *
from accounts.constants import Params
import logging
log = logging.getLogger('accounts')


class UserDbService(object):

    @staticmethod
    def save_signup_user_data(data, session):
        """
        on successful user registration save the user_id and token(auth_key) in current session
        :param data: signup form data
        :param session: current session
        :return: signup status
        """
        validation_status = user_info_validate_data(data)
        if validation_status != "success":
            return {"data": validation_status, "statusCode": 205}
        user = User.objects.filter(email_id=data["email"]).first()
        if not user:
            session_key = session.session_key
            auth_key = hash(data["email"] + session_key)
            hash_password = make_password(data["password"])
            user = User(password=hash_password, email_id=data["email"])
            user.first_name = data["first_name"]
            if data["last_name"]:
                user.last_name = data["last_name"]
            user.phone_number = data["phone_no"]
            if data["gender"].lower() in Params:
                user.gender = Params[data["gender"].lower()]
            user.last_login = timezone.now()
            user.date_joined = timezone.now()
            user.save()
            save_user_auth_key(session, user.user_id, auth_key)
            return {"data": "You are successfully Sign Up", "token": str(auth_key), "statusCode": 200}
        return {"data": "This E-Mail is already exist, Please Sign In", "statusCode": 205}

    @staticmethod
    def signin_user(data, session):
        """
        on successful user login save the user_id and token(auth_key) in current session
        :param data: login data
        :param session: current session
        :return: login status
        """
        session_key = session.session_key
        auth_key = hash(data["email"] + session_key)
        user = User.objects.filter(email_id=data["email"].strip()).first()

        if not user:
            return {"data": "Enter E-Mail is not registered, Please Sign Up", "statusCode": 205}
        elif not check_password(data["password"], user.password):
                return {"data": "Please Enter the Correct Password", "statusCode": 205}
        elif user.is_active:
            save_user_auth_key(session, user.user_id, auth_key)
            user.last_login = timezone.now()
            user.save()

            return {"data": "You are successfully Sign In", "token": str(auth_key), "statusCode": 200}
        else:
            return {"data": "Sorry! You are not Active User", "statusCode": 205}
