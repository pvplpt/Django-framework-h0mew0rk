from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField(min_value=0, max_value=42)
    

class ImageForm(forms.Form):
    image = forms.ImageField()