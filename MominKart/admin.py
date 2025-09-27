from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem,Laptop,Watch,Mobile,Book,Clothing

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("product", "quantity", "price")
    extra = 0
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "total", "status", "created_at")
    inlines = [OrderItemInline]

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Laptop)
admin.site.register(Watch)
admin.site.register(Mobile)
admin.site.register(Book)
admin.site.register(Clothing)
