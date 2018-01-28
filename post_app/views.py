from accounts.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib import messages
from post_app.models import *
import logging
log = logging.getLogger('post_app')
from post_app.post_db_service import *
post_db_service = PostDbService()


class Home(APIView):
    def get(self, request):
        """
           home page with all post data.
           :param request:
           :return: Response as home page with data
           """
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            post_details = post_db_service.get_all_post_details(user)
            return render(request, 'home.html', {"name": user.get_full_name(), "post_details_list": post_details})
        except Exception, e:
            log.debug(str(e) + " IN Home PostRestApi")
            return Response({"data": "failure", "statusCode": 404})


class SaveNewPost(APIView):
    def post(self, request):
        """ Save new post and return the same post details"""
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            post_details = post_db_service.save_post_data(user, request.data)
            return Response({"data": "success", "post_details": post_details, "statusCode": 200})
        except Exception, e:
            log.debug(str(e) + " IN SaveNewPost PostRestApi")
            return Response({"data": "failure", "statusCode": 404})


class Like(APIView):
    def post(self, request):
        """ update the post like """
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            like_details = post_db_service.update_post_like(user, request.data["post_id"])
            return Response({"data": "success", "like_details": like_details, "statusCode": 200})
        except Exception, e:
            log.debug(str(e) + " IN SaveNewPost PostRestApi")
            return Response({"data": "failure", "statusCode": 404})