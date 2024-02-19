from django.urls import re_path as url
# from AppTwo import views
from AppTwo import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
]