from django.shortcuts import render
from django.http import HttpResponse 
from .models import * 

# Create your views here.

def home(request):
    orders = Order.objects.all() 
    customers = Customer.objects.all() 

    total_customers = customers.count() 
    total_orders = orders.count() 
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    
    return render(request,'dashboard.html',{"orders":orders,"customers":customers,"total_orders":total_orders,"delivered":delivered,"total_customers":total_customers,"pending":pending})


def products(request):
    products = Product.objects.all() 
    return render(request,'products.html', {'products':products})


def customer(request):
    return render(request,'customer.html')