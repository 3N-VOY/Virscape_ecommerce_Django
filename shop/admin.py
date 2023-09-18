from django.contrib import admin
from .models import Category, Item
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
