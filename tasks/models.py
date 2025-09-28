from django.db import models
class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    start_date=models.DateTimeField()
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name
    

class Task(models.Model):
    STATUS_CHOICES=[
        ('PENDING','panding'),
        ('IN_PROGRESS','in_progress'),
        ('COMPLETED','completed'),
    ]
    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        default=1,
        related_name='tasks'
        )
    assigned_to =models.ManyToManyField(Employee,related_name='tasks')
    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=15,choices=STATUS_CHOICES,default='PENDING')
    is_completed=models.BooleanField(default=False)
    creted_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title




class TaskDetail(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OPTIONS=(
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='details'
        ) #Task entity/table er stahe relation
    assigned_to = models.CharField(max_length=100)
    priority=models.CharField(max_length=1, choices=PRIORITY_OPTIONS ,default=LOW)
    notes=models.TextField(blank=True,null=True)
    def __str__(self):
        return f'Details form Task {self.task.title}'
    


