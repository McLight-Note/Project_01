from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductForm
from .models import Product

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