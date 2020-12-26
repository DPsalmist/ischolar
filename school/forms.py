from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)


class PayFeesForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    Phone_no = forms.FloatField()
    Amount = forms.FloatField()
    student_class = forms.CharField(max_length=50)
    term = forms.CharField(max_length=50)
    session = forms.CharField(max_length=50)
    remarks = forms.CharField(max_length=50)