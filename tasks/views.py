from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail,Project
from datetime import date
from django.db.models import Q #for OR 
from django.db.models import Count,Max,Min,Avg
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
            # Query for Database
    """retrive all data from tasks model"""
    # task=Task.objects.all()
    """retrive a specific task"""
    # task_3 = Task.objects.get(id=3)
    """fetch the first task"""
    # first_task = Task.objects.first()

    """show the task that are COMPLETED"""
    # tasks=Task.objects.filter(status="COMPLETED")
    """show the task which due date today""" 
    # tasks=Task.objects.filter(due_date=date.today())
    """show tha task whose riority is not low"""
    # tasks=TaskDetail.objects.exclude(priority="L")
    """show tha task that single condition """
    # tasks=Task.objects.filter(title__icontains="c")
    """show tha task that double(AND) condition """
    # tasks=Task.objects.filter(title__icontains="c",status="PENDING")
    """show tha task that double(OR) condition """
    # tasks=Task.objects.filter(Q(status="PENDING")|Q(status="IN_PROGRESS"))
    """select related (OneToOneField)"""
    # tasks=Task.objects.select_related("details").all()
    # tasks=TaskDetail.objects.select_related("task").all()
    """select related (foreignkey)"""
    # tasks=Task.objects.select_related("project").all()
    """prefetch related (reverse foreignkey and ManyToManyField)"""
    # tasks=Project.objects.prefetch_related("tasks").all() #for reverse foreignkey
    # tasks=Task.objects.prefetch_related("assigned_to").all()#for ManyToManyField
    
    """aggregation"""
    # task_count=Task.objects.aggregate(num_task=Count('id'))
    """annotate"""
    projects=Project.objects.annotate(task_in_project=Count('tasks')).order_by('task_in_project')
    return render(request,'show_task.html',{'projects':projects})

  

    
