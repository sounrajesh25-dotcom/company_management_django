from django.shortcuts import render,redirect
from .models import Company,employee
from .forms import CompanyForm,employeeForm

# Create your views here.

def company_list(request):
    companies=Company.objects.all()
    return render (request,'company_app/company_list.html',{'companies':companies})

def company_create(request):
    form=CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('company_list')
    return render(request,'company_app/company_form.html',{'form':form})

def employee_list(request):
    employees=employee.objects.select_related('company')
    return render(request,'company_app/employee_list.html',{'employees':employees})

def employee_create(request):
    form=employeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request,'company_app/employee_form.html',{'form':form})
    
