from accounts.constants import login_not_required, admin_login_not_required
from django.shortcuts import redirect


class BeforeRequest(object):
    def __init__(self, get_response):
        """ Global state can be set in Python __init__ method """
        self.get_response = get_response

    def is_admin_url(self, route):
        url = str(route)
        url = url.split('/')
        if 'admin' in url:
            return True
        return False

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        before getting in to the view, authenticate each request
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """
        if not request.session.get('has_session'):
            request.session['has_session'] = True
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session = request.session

        url = request.path_info

        # admin login authentication
        if self.is_admin_url(url):
            if url in admin_login_not_required:
                pass
            elif not request.user.is_authenticated():
                    return redirect('/admin')

        elif url in login_not_required:
            pass
        elif 'auth_key' not in session:
            return redirect('/')
        elif request.content_type in ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data']:

            auth_key = session['auth_key']
            import json
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            token = body['token']
            # print (token, auth_key)
            if str(token) != str(auth_key):
               return redirect('/logout/')
        elif 'auth_key' in session and request.content_type == "text/plain":
            pass
        else:
            return redirect('/')

    # def process_response(self, request, response):
    #     pass
    #
    # def process_exception(self, request, exception):
    #     """ Called when a view raises an exception."""
    #     pass

