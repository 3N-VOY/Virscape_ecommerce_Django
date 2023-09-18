from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from django.http import JsonResponse, HttpResponse
import json
from shop.models import Item
from userprofiles.models import Profile
from django.conf import settings
from django.contrib.auth.decorators import login_required 
from userprofiles.forms import SignUpForm
import stripe
import time
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    
    context = {'items':items, 'order':order}
          
    return render(request,'cart/cart_view.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    
    context = {'items':items, 'order':order}
    
    
    return render(request, 'cart/checkout.html', context)

def updateItem(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
       
        
        print('Action:', action)
        print('productId:', productId)

        customer = request.user.profile
        product = Item.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == "remove":
            orderItem.quantity = (orderItem.quantity - 1)
        
        elif action == "trash":
            orderItem.quantity = 0
          
          
            
        orderItem.save()
        
        if orderItem.quantity <= 0:
            orderItem.delete()
        
        
        return JsonResponse('Item was added', safe=False)
       
       
def payment_cancel(request):
    return render(request, 'cart/payment-failed.html')


def payment_success(request):
    return render(request, 'cart/payment-completed.html')




def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    # Get the user's order and related items
    customer = request.user.profile if request.user.is_authenticated else None
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_items = order.orderitem_set.all()

    # Create line items for the Stripe session
    line_items = []
    for item in order_items:
        line_item = {
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': item.product.title,  # Replace with your item name
                },
                'unit_amount': int(item.product.price * 100),  # Convert price to cents
            },
            'quantity': item.quantity,
        }
        line_items.append(line_item)

    # Create the Stripe Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=f'{settings.WEBSITE_URL}payment_success/',
        cancel_url=f'{settings.WEBSITE_URL}payment-failed/',
    )
    return JsonResponse({'id': session.id})



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

