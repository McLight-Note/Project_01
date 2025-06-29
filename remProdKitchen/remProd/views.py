from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import ProductForm
from .models import Product
import json
from datetime import datetime
import os

# Create your views here.

def home_view(request):
    return render(request, 'remProd/home.html')

def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'remProd/product_form.html', {'form':form})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'remProd/product_list.html', {'products':products})

def product_update_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'remProd/product_form.html', {'form':form})

def product_delete_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'remProd/product_confirm_delete.html', {'product':product})

def decrease_quantity_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        decrease_amount = int(request.POST.get('decrease_amount', 1))
        if product.quantity >= decrease_amount:
            product.quantity -= decrease_amount
            product.save()
        return redirect('product_list')
    return render(request, 'remProd/decrease_quantity.html', {'product': product})

def export_inventory_view(request):
    """Export inventory data to a text file"""
    products = Product.objects.all()
    
    # Create export data
    export_data = {
        'export_date': datetime.now().isoformat(),
        'total_products': products.count(),
        'products': []
    }
    
    for product in products:
        product_data = {
            'product_id': product.product_id,
            'name': product.name,
            'quantity': product.quantity,
            'image_path': str(product.image) if product.image else None
        }
        export_data['products'].append(product_data)
    
    # Create response
    response = HttpResponse(
        json.dumps(export_data, indent=2, ensure_ascii=False),
        content_type='application/json'
    )
    response['Content-Disposition'] = f'attachment; filename="inventory_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json"'
    
    return response

def export_text_view(request):
    """Export inventory data to a simple text file"""
    products = Product.objects.all()
    
    # Create simple text format
    text_content = f"Inventory Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    text_content += "=" * 50 + "\n\n"
    text_content += f"Total Products: {products.count()}\n\n"
    
    for product in products:
        text_content += f"Product ID: {product.product_id}\n"
        text_content += f"Name: {product.name}\n"
        text_content += f"Quantity: {product.quantity}\n"
        if product.image:
            text_content += f"Image: {product.image}\n"
        text_content += "-" * 30 + "\n\n"
    
    # Create response
    response = HttpResponse(text_content, content_type='text/plain; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="inventory_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt"'
    
    return response

def import_inventory_view(request):
    """Import inventory data from a text file"""
    if request.method == "POST":
        if 'inventory_file' in request.FILES:
            uploaded_file = request.FILES['inventory_file']
            
            try:
                # Read and parse the uploaded file
                content = uploaded_file.read().decode('utf-8')
                data = json.loads(content)
                
                imported_count = 0
                updated_count = 0
                
                for product_data in data.get('products', []):
                    product_id = product_data.get('product_id')
                    name = product_data.get('name')
                    quantity = product_data.get('quantity')
                    
                    if product_id and name is not None and quantity is not None:
                        # Try to update existing product or create new one
                        product, created = Product.objects.update_or_create(
                            product_id=product_id,
                            defaults={
                                'name': name,
                                'quantity': quantity
                            }
                        )
                        
                        if created:
                            imported_count += 1
                        else:
                            updated_count += 1
                
                messages.success(request, f'Successfully imported {imported_count} new products and updated {updated_count} existing products.')
                
            except json.JSONDecodeError:
                messages.error(request, 'Invalid JSON file format.')
            except Exception as e:
                messages.error(request, f'Error importing data: {str(e)}')
        else:
            messages.error(request, 'Please select a file to import.')
    
    return render(request, 'remProd/import_inventory.html')

def backup_inventory_view(request):
    """Create a backup of current inventory"""
    products = Product.objects.all()
    
    # Create backup directory if it doesn't exist
    backup_dir = 'backups'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Create backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"inventory_backup_{timestamp}.txt"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    try:
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(f"Inventory Backup - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            
            for product in products:
                f.write(f"Product ID: {product.product_id}\n")
                f.write(f"Name: {product.name}\n")
                f.write(f"Quantity: {product.quantity}\n")
                if product.image:
                    f.write(f"Image: {product.image}\n")
                f.write("-" * 30 + "\n")
        
        messages.success(request, f'Backup created successfully: {backup_filename}')
        
    except Exception as e:
        messages.error(request, f'Error creating backup: {str(e)}')
    
    return redirect('product_list')