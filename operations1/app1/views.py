from django.db.models.expressions import result
from django.db.models.fields import return_None
from django.shortcuts import render
from app1.forms import AdditionForm
def addition(request):
    if(request.method=='POST'):
        print(request.POST)
        return render(request,'addition.html')
    form_instance=AdditionForm()
    return render(request,'addition.html',{'form':form_instance})

from app1.forms import FactForm
def factorial(request):
    if(request.method=='POST'):
        print(request.POST)
        return  render(request,'factorial.html')
    form_instance=FactForm()
    return render(request,'factorial.html',{'form':form_instance})

from app1.forms import BmiForm
def bmi(request):
    if (request.method == 'POST'):
        print(request.POST)
        return render(request, 'bmi.html')
    form_instance = BmiForm()
    return render(request, 'bmi.html', {'form': form_instance})

from app1.forms import signupForm
def signup(request):
    if (request.method == 'POST'):
        print(request.POST)
        return render(request, 'signup.html')
    form_instance = signupForm()

    return render(request, 'bmi.html',{'form':form_instance})

# from app1.forms import calorieForm
# def calorie(request):
#     if (request.method == 'POST'):
#         print(request.POST)
#         return render(request, 'calorie.html')
#     form_instance = calorieForm()
#
#     return render(request, 'calorie.html',{'form':form_instance})
from app1.forms import calorieForm
def calorie(request):
        if (request.method == 'POST'):  ##after form submission
            print(request.POST)

            ##creating form object using data submitted by user

        form_instance=calorieForm(request.POST)

        ##checks the validity of data using is_valid()
        if form_instance.is_valid():

            ##accessing the cleaned data after validation
            data=form_instance.cleaned_data
            Height=(data['Height'])
            Weight=(data['Weight'])
            print(type('Height'))
            Gender=(data['Gender'])
            Age=(data['Age'])
            Activity_level=(data['Activity_level'])
            print(type(Activity_level))
            print(Height,Weight,Gender,Age,Activity_level)
            if Gender=='male':
                bmr=((10*Weight)+(6.25*Height)-(5*Age)+5)

            else:
                bmr=((10*Weight)+(6.25*Height)-(5*Age)-161)

            calorie=bmr*float(Activity_level)
            print(calorie)

            return render(request, 'calorie.html',{'form':form_instance,'result':calorie})

        form_instance=calorieForm()
        return render(request,'calorie.html',{'form':form_instance})