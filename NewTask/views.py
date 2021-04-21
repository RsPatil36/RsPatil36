from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from . import forms,models
from django.contrib import messages

from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    if request.method == "POST":
        if request.POST.get("Name") and request.POST.get("URL") and request.POST.get("Phone_Number"):
            form = forms.UserRegisterForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.success(request,'Record saved successfully...')
                return render(request, 'success.html',{'name':form})

    else:
        form = forms.UserRegisterForm()
    return render(request, 'index.html', {'form': form})

def check_name(request):
    if request.method == "POST":
        if request.POST.get("Name"):
            form = forms.Check_Name(request.POST)
            if form.is_valid():
                Name = request.POST['Name']
                try:
                    emp = models.Data_saving_db.objects.get(Name=Name)
                    return render(request, 'result.html', {'name': emp})
                except ObjectDoesNotExist:
                    emp =None
                    return render(request, 'result.html', {'name': emp})

    else:
        form = forms.Check_Name()
    return render(request, 'index.html', {'form': form})