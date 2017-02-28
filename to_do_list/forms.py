from django import forms

class TaskForm(forms.Form):
    text = forms.CharField(label='Task Name', max_length=200)
    duration = forms.DurationField(label='Expected duration. Format: "(DD) HH:MM:SS"')
