from django.urls import re_path as url
# from AppTwo import views
from AppTwo import views

urlpatterns = [
    url(r'^users/', views.users, name='users'),
    url(r'^form/', views.users_form, name='users'),
]