from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

def home_view(request):
    return render(request, 'remProd/home.html')

def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'remProd/product_form.html', {'form':form})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'remProd/product_list.html', {'products':products})

def product_update_view(request, name):
    product = Product.objects.get(name=name)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'remProd/product_form.html', {'form':form})

def product_delete_view(request, name):
    product = Product.objects.get(name=name)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'remProd/product_confirm_delete.html', {'product':product})