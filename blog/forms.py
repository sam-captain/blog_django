from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label ='your name', max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number =forms.CharField(widget= forms.NumberInput)
    message = forms.CharField(widget = forms.Textarea)

class mailform(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    recipient =forms.EmailField(max_length=100)