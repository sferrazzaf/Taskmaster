from django import forms

class TaskForm(forms.Form):
    text = forms.CharField(label='Describe the task', max_length=200)
