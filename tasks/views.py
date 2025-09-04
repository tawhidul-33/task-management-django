from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # work with database
    # transform data
    # data pass
    # http Response /json Response
    return HttpResponse("welcom to the task mmenagement system")
def contact(request):
    return HttpResponse("<h1 style='color:red'>This is contact list</h1>")

def show_task(request):
    return HttpResponse("this is show task")
def show_specific_task(request , id):

    return HttpResponse(f" this is apecific page {id}")