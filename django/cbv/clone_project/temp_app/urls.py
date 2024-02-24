from django.urls import re_path as url
from temp_app import views

app_name = 'temp_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create_school/$',views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(), name='delete'),
    url(r'create_student', views.StudentCreateView.as_view(),name='create_student'),
]
