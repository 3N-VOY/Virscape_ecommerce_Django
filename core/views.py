from django.shortcuts import render, get_object_or_404
from shop.models import Category, Item
# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    newest_items = Item.objects.order_by('-created_date')[:8]
    context = {'categories':categories,'newest_items':newest_items}
    
    return render(request, "core/homepage.html", context)



def about(request):
    return render(request, 'core/about.html')

def faqs(request):
    return render(request, 'core/faqs.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def shipping_return(request):
    return render(request, 'core/shipping_return.html')

def terms_service(request):
    return render(request, 'core/terms_service.html')