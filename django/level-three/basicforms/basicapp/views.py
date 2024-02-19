from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def form_name_views(request):
    form = forms.FormName()
    form_dict = {'form':form}

    # check request
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something with the data retrivied
            print("VALIDAITON SUCCESS!")
            print(f'Name: {form.cleaned_data["name"]}')
            print(f'Email: {form.cleaned_data["email"]}')
            print(f'Text: {form.cleaned_data["text"]}')


    return render(request, 'basicapp/forms_page.html', form_dict)


