from django.shortcuts import render
from AppTwo.models import User
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("<em>Welcome to My Second Project</em>")


def index(request):
    return render(request,'apptwo/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'apptwo/users.html',context=user_dict)