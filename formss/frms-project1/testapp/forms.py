from django import forms
class studentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()
    rollno=forms.IntegerField() 