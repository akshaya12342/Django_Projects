from django.shortcuts import render,redirect
from employee.models import Employee
from employee.forms import employeeForm
# Create your views here.

def employee_list(request):
    e=Employee.objects.all()
    print(e)
    return render(request,'employee_list.html',{'employee':e})

def create_employee(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        form_instance = employeeForm(request.POST, request.FILES)
        if form_instance.is_valid():
            e=Employee.objects.create(name=form_instance.cleaned_data['name'],
                                      age=form_instance.cleaned_data['age'],
                                      salary=form_instance.cleaned_data['salary'],
                                      designation=form_instance.cleaned_data['designation'],
                                      place=form_instance.cleaned_data['place'],
                                      department_name=form_instance.cleaned_data['department_name'],
                                      image=form_instance.cleaned_data['image'])
            e.save()
            return redirect('employee_list')
    form_instance=employeeForm()
    return render(request,'create_employee.html',{'form':form_instance})


def editemployee(request,i):
    e=Employee.objects.get(id=i)
    if(request.method=="POST"):
        form_instance=employeeForm(request.POST,request.FILES,instance=e)
        if(form_instance.is_valid()):
            form_instance.save()
            return redirect('employee_list')
    form_instance=employeeForm(instance=e)
    return render(request,'editemployee.html',{'form':form_instance})


def deleteemployee(request,i):
    e=Employee.objects.get(id=i)
    e.delete()
    return redirect('employee_list')

def displayemployee(request,i):
    e=Employee.objects.get(id=i)
    return render(request,'displayemployee.html',{'employee':e})
