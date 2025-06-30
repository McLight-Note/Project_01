from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse, Http404
from django.conf import settings
import os
from .forms import ProductForm
from .models import Product

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

def health_check(request):
    return HttpResponse("OK", content_type="text/plain")

def serve_media(request, path):
    """Custom view to serve media files in production"""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    # Debug information
    print(f"Requested path: {path}")
    print(f"Full file path: {file_path}")
    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"File exists: {os.path.exists(file_path)}")
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read())
            # Set appropriate content type based on file extension
            if path.endswith('.jpg') or path.endswith('.jpeg'):
                response['Content-Type'] = 'image/jpeg'
            elif path.endswith('.png'):
                response['Content-Type'] = 'image/png'
            elif path.endswith('.webp'):
                response['Content-Type'] = 'image/webp'
            elif path.endswith('.gif'):
                response['Content-Type'] = 'image/gif'
            else:
                response['Content-Type'] = 'application/octet-stream'
            return response
    else:
        raise Http404(f"File not found: {file_path}")

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'remProd/dashboard.html')

@login_required
def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'remProd/product_form.html', {'form':form})

@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'remProd/product_list.html', {'products':products})

@login_required
def product_update_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'remProd/product_form.html', {'form':form})

@login_required
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'remProd/product_confirm_delete.html', {'product':product})

@login_required
def decrease_quantity_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        decrease_amount = int(request.POST.get('decrease_amount', 1))
        if product.quantity >= decrease_amount:
            product.quantity -= decrease_amount
            product.save()
            messages.success(request, f'Quantity decreased by {decrease_amount}')
        else:
            messages.error(request, 'Not enough quantity to decrease')
        return redirect('product_list')
    return render(request, 'remProd/decrease_quantity.html', {'product': product})

@login_required
def update_quantity_view(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, product_id=product_id)
        action = request.POST.get('action')
        amount = int(request.POST.get('amount', 1))
        
        if action == 'increase':
            product.quantity += amount
            product.save()
            messages.success(request, f'Quantity increased by {amount}')
        elif action == 'decrease':
            if product.quantity >= amount:
                product.quantity -= amount
                product.save()
                messages.success(request, f'Quantity decreased by {amount}')
            else:
                messages.error(request, 'Not enough quantity to decrease')
        
        return redirect('product_list')
    
    return redirect('product_list')