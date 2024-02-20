from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import NewUserForm
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

def users_form(request):
    
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    form_dict = {'form':form}
    return render(request,'apptwo/users_form.html',form_dict)