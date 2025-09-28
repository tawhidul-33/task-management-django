from django.urls import path
from tasks.views import manager_dashboard, user_dashboard,test,create_task_form,view_task

urlpatterns=[
path('manager-dashboard/',manager_dashboard),
path('user-dashboard/',user_dashboard),
path('test/',test),
path('create_task_form/',create_task_form),
path('view_task/',view_task)
]