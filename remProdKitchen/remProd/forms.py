from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'image']
        labels = {
            'name': 'Product Name',
            'quantity': 'Quantity',
            'image': 'Product Image',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter product name',
                    'class': 'form-control',
                    'required': True,
                    'minlength': '2',
                    'maxlength': '100'
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter quantity',
                    'class': 'form-control',
                    'required': True,
                    'min': '0',
                    'step': '1'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*'
                }
            ),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            name = name.strip()
            if len(name) < 2:
                raise forms.ValidationError("Product name must be at least 2 characters long.")
            if len(name) > 100:
                raise forms.ValidationError("Product name cannot exceed 100 characters.")
        return name
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity