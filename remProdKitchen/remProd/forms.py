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
                    'accept': 'image/webp,image/png,image/jpeg,image/jpg,image/gif,image/bmp,image/tiff',
                    'onchange': 'previewImage(this)'
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
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Image file size must be under 5MB.")
            
            # Check file extension
            allowed_extensions = ['.webp', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
            file_extension = image.name.lower()
            if not any(file_extension.endswith(ext) for ext in allowed_extensions):
                raise forms.ValidationError(
                    "Please upload a valid image file. Supported formats: WebP, PNG, JPG, JPEG, GIF, BMP, TIFF"
                )
            
            # Additional validation for image content
            try:
                from PIL import Image
                img = Image.open(image)
                img.verify()  # Verify it's actually an image
                image.seek(0)  # Reset file pointer
            except Exception:
                raise forms.ValidationError("The uploaded file is not a valid image.")
        return image