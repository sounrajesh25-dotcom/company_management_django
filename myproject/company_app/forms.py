from django import forms


from .models import Company,employee

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'
class employeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'

    