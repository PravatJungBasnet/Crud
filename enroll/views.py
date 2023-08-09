from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.
def base(request):
    return render(request,'enroll/base.html')
def add(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']
            register=Student(name=nm,email=em,password=pas)
            register.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    std=Student.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':std})
# delete
def delete(request,id):
    if request.method=='POST':
        dl=Student(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')
        

        
        

def update(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
    

    return render(request,'enroll/update.html')
