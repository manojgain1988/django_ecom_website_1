from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
