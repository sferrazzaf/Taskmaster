from django import forms

class TaskForm(forms.Form):
    text = forms.CharField(label='Enter new task', max_length=200)
