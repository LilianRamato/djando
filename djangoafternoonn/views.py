from django.shortcuts import render
from djangoafternoonn.form import EmpForm
def Home(request):
    return render(request, 'index.html')

def About_us(request):
    return render(request,'About_Us.html')
def service(request):
    return render(request,'myservices.html')
def contact(request):
    return render(request,'contactus.html')
def myform(request):
    stu=EmpForm()
    return render(request,'forms.html',{'form':stu})