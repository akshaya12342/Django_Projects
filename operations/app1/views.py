from django.db.models.expressions import result
from django.db.models.fields import return_None
from django.shortcuts import render
def addition(request):
    if(request.method=='POST'):
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        result=int(n1)+int(n2)
        # print(result)
        context={'result':result}
        return render(request,'addition.html',context)
# Create your views here.


    return render(request,'addition.html')

def factorial(request):
    if(request.method=='POST'):
        n=int(request.POST['num'])
        f=1
        for i in range(1,n+1):
            f=f*i
        context={'result':f}
        return render(request,'factorial.html',context)
    return render(request,'factorial.html')

def bmi(request):
    if(request.method=='POST'):
        h1=int(request.POST['h'])
        w1=int(request.POST['w'])
        h2=h1/100
        result1=int(w1/(h2**2))
        context={'result':result1}
        return render(request, 'bmi.html', context)

    return render(request, 'bmi.html')