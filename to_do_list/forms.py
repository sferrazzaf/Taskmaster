from django import forms

class TaskForm(forms.Form):
    text = forms.CharField(label='Enter new task', max_length=200)
    duration = forms.DurationField(label='Enter expected duration. Format: "(DD) HH:MM:SS"')
