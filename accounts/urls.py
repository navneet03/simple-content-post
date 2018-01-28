from django.conf.urls import url
from accounts import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',  RedirectView.as_view(url='/signup/')),

    url(r'^signup/$', views.signup_template, name='signup_template'),
    url(r'^save_signup_info/', views.SaveSignUpInfo.as_view()),
    url(r'^login/', views.SignIn.as_view()),
    url(r'^logout/$', views.LogOut.as_view()),
]
