from django.conf.urls import include, url
from django.contrib import admin

# from django.contrib.auth import views as auth_views

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accounts.urls')),
    url(r'^', include('post_app.urls')),
]
