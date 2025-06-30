from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponse
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