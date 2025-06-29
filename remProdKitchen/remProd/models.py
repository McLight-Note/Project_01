from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(
        upload_to='product_images/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['webp', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'],
                message='Please upload a valid image file. Supported formats: WebP, PNG, JPG, JPEG, GIF, BMP, TIFF'
            )
        ],
        help_text='Supported formats: WebP, PNG, JPG, JPEG, GIF, BMP, TIFF (Max 5MB)'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"