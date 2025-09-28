from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task
# Create your views here.
def manager_dashboard(request):
    return render(request,'dashboard/manager_dashboard.html')

def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")

def test(request):
    names=["siyam","sohan","rohul","simul"]
    counts=0
    for name in names:
        counts += 1 
    context={
        "names":names,
        "age": 22,
        "count":counts
    }
    return render(request,'test.html',context)



def create_task_form(request):
    # employees  = Employee.objects.all()
    form=TaskModelForm() #for GET method
    if request.method =="POST":
        form=TaskModelForm(request.POST)
        if form.is_valid():
            """for Django Model form data"""
            form.save()
            return render(request,"task_form.html",{"form":form,"message":"Task Added Successfull"})
    context={
        "form":form
    }
    return render(request,"task_form.html",context)


def view_task(request):
    #retrive all data from tasks model
    task=Task.objects.all()
    #retrive a specific task
    task_3 = Task.objects.get(id=3)
    #fetch the first task
    first_task = Task.objects.first()
    return render(request,'show_task.html',{'tasks':task ,'task_3':task_3,'first_task':first_task})
    
