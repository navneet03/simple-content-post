from django.conf.urls import url
from post_app import views

urlpatterns = [
    url(r'^home/', views.Home.as_view()),
    url(r'^save_new_post/', views.SaveNewPost.as_view()),
    url(r'^like/', views.Like.as_view()),
]
