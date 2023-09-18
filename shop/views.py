from django.shortcuts import render, get_object_or_404
from .models import Item, Category
from django.db.models import Q

# Create your views here.
def shop(request):
    item = Item.objects.all()
    context = {'item':item}
    return render(request, 'shop/shop.html', context)

def view_item(request, category_slug, slug):
    item = get_object_or_404(Item, slug=slug)
    context = {'item': item}
    return render(request, 'shop/item_detail.html', context)

def search_item(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        items = Item.objects.filter(Q(title__icontains=search_query) | Q(price__contains=search_query) | Q(description__icontains=search_query))
        context = {'query':search_query, 'items':items}
        return render(request, 'shop/search_results.html', context)
    else:
        return render(request, 'shop/search_results.html', context)
        
        
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {'category':category}
    return render(request, 'shop/category_detail.html', context)


