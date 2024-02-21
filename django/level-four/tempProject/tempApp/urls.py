# Here is where we set the realtive url path
from django.urls import re_path as url
from tempApp import views


# TEMPLATE TAGGING
app_name = 'tempApp'

urlpatterns = [
    url(r'^relative/$',views.relative, name='relative'),
    url(r'^other/$',views.other, name='other')
]