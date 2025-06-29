from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id' : 'Product ID',
            'name' : 'Product Name',
            'quantity' : 'Quantity',
         }
        widgets = {
            'product_id' : forms.NumberInput(
                attrs={'placeholder' : 'ID',
                       'class':'form-control'}
            ),
            'name' : forms.TextInput(
                attrs={'placeholder' : 'product name',
                       'class':'form-control'}
            ),
            'quantity' : forms.NumberInput(
                attrs={'placeholder' : '0',
                       'class':'form-control'}
            ),
        }