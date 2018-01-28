from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from accounts.user_db_service import *
user_db_service = UserDbService()

import logging
log = logging.getLogger('accounts')


def signup_template(request):
    """
    User registration template view.
    if user is already login then redirect to home page
    :param request:
    :return: Response as signup page.
    """
    if 'user_id' in request.session:
        return HttpResponseRedirect('/home/')
    return render(request, 'signup.html')


class SaveSignUpInfo(APIView):
    def post(self, request):
        """
        New user Registration
        :param request: get the user registration data
        :return: Response: after successful registration token and user name
        """
        try:
            session = request.session
            data = request.data
            resp_data = user_db_service.save_signup_user_data(data, session)
            return Response(resp_data)
        except Exception, e:
            log.debug(str(e) + " IN SaveSignUpInfo PostRestApi")
            return Response({"data": "failure", "statusCode": 404})


class SignIn(APIView):
    def post(self, request):
        """
        Login view
        :param request: login request with email and password
        :return: Response: after successful login token and user name
        """
        try:
            session = request.session
            data = request.data
            resp_data = user_db_service.signin_user(data, session)
            return Response(resp_data)
        except Exception, e:
            log.debug(str(e) + " IN SignIn PostRestApi")
            return Response({"data": "failure", "statusCode": 404})


class LogOut(APIView):
    def get(self, request):
        """
        Logout view; delete the current session
        :param request:
        :return: Redirect to signup page
        """
        try:
            request.session.flush()
            if 'user_id' in request.session:
                del request.session['user_id']
            if 'auth_key' in request.session:
                del request.session['auth_key']
            request.session.modified = True
            return HttpResponseRedirect('/signup/')
        except Exception, e:
            log.debug(str(e) + " IN LogOut PostRestApi")
            return Response({"data": "failure", "statusCode": 404})


