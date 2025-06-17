from django import forms

from employee.models import Employee
class employeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','age','salary','designation','place','department_name','image']

