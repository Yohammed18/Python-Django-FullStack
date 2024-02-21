from django.shortcuts import render
# from django.http import HttpResponse

# 


# def index(request):
#     return HttpResponse('Hello World')

def index(request):
    return render(request,'tempApp/index.html')

def other(request):
    return render(request,'tempApp/other.html')

def relative(request):
    return render(request,'tempApp/relative_url_templates.html')