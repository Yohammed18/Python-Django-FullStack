"""clone_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path as url
from temp_app import views



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^temp_app/',include('temp_app.urls', namespace='temp_app'))

    # returning a base class view
    # url(r'^$', views.CBView.as_view())
    # url(r'^$', views.index, name='home')
]
