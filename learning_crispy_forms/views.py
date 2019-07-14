from django.shortcuts import render
from django.http import HttpResponse
from learning_crispy_forms import forms

# Create your views here.
def index(request):
    my_dict={'insert_me':"I m inserted"}
    return render(request,'learning_crispy_forms/index.html',context=my_dict)

def form_name_view(request):
    form=forms.FormName()
    if request.method == 'POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("Name is:")

    return render(request,'learning_crispy_forms/formpage.html',{'form':form})

