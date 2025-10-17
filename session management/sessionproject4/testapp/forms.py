from django import forms 
class AddItemsForm(forms.Form):
    itemname=forms.CharField()
    quantity=forms.IntegerField()


