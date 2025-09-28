from django import forms 
from tasks.models import Task

#Django Forms
class TaskForm(forms.Form):
    title=forms.CharField(max_length=250 )
    description=forms.CharField(widget=forms.Textarea,label="Task Description")
    due_date=forms.DateField(widget=forms.SelectDateWidget,label="Due Date")
    assigned_to= forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=[] ,label="Assign_To")
    def __init__(self, *args,**kwargs):
        employees =kwargs.pop("employees",[])
        super().__init__(*args,**kwargs)
        self.fields['assigned_to'].choices=[(emp.id,emp.name)for emp in employees]



        

"""Mixing to apply style to fields"""
class StyleedForMixin:
    default_classes=" border-2 border-gray-300 w-full rounded-lg shadow-sm focus:outline-none focus:border-rose-500"
    def apply_styled_widgets(self):
     for field_name,field in self.fields.items():
        if isinstance(field.widget,forms.TextInput):
            field.widget.attrs.update({
                'class':self.default_classes,
                'placeholder':f'Enter {field.label.lower()}'
            })
        elif isinstance(field.widget,forms.Textarea):
            field.widget.attrs.update({
               'class':self.default_classes,
               'placeholder':f'Enter {field.label.lower()}', 
               'rows': 5

            })
        elif isinstance(field.widget,forms.SelectDateWidget):
            field.widget.attrs.update({
                'class':self.default_classes,
                'class':'bg-pink-300 rounded'
            })
        elif isinstance(field.widget,forms.CheckboxSelectMultiple):
            field.widget.attrs.update({
                'class':'space-y-2',
            })
        else:
            field.widget.attrs.update({
                'class':self.default_classes,
            })
            




#Django Model Form
class TaskModelForm(StyleedForMixin,forms.ModelForm):
    class Meta:
        model= Task
        fields= ['title','description','due_date','assigned_to']      #jei gola show korte chai 
                                                                      #or
        # exclude=['project','is_completed','creted_a','updated_at']  #jaita jeita show na kore
        """Manual widget """
        # widgets={
        #     'title':forms.TextInput(attrs={
        #         "class":" border border-gray-300 w-full rounded-lg shadow-sm focus:border-blue-100 px-4  ",
        #         "placeholder":"Enter task title", 
        #       }
        #     ),
        #     'description':forms.Textarea(attrs={
        #         "class":" border border-gray-300 w-full rounded-lg shadow-sm focus:border-blue-100 m-2 px-4 h-12 bg-blue-600",
        #         "placeholder":"Discribe the task", 
        #       }),
        #     'due_date':forms.SelectDateWidget(attrs={
        #         "class":"border border-gray-300 w-full rounded-lg shadow-sm focus:border-blue-100 bg-gray-300",
         
        #       }),
        #     'assigned_to':forms.CheckboxSelectMultiple
        # }
        widgets={
           'due_date':forms.SelectDateWidget,
           'assigned_to':forms.CheckboxSelectMultiple
        }
        
    """widget using mixing"""   
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.apply_styled_widgets()
