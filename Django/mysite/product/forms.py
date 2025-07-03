from django import forms


class productForm(forms.Form):
    name = forms.CharField(initial='Enter your name')
    email = forms.EmailField(initial='Enter your email')
    message = forms.CharField(initial='Enter your message')