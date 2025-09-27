from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, CartItem, Order, OrderItem,Laptop,Watch,Mobile,Book,Clothing
from .forms import CheckoutForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms   # ✅ ये add करना जरूरी है


# Homepage
#def homepage(request):
  #  products = Product.objects.all()
  #  return render(request, "index.html", {'products': products})

def homepage(request):
    query = request.GET.get('q')  # GET parameter 'q' को पकड़ो
    if query:
        products = Product.objects.filter(name__icontains=query)  # case-insensitive search
    else:
        products = Product.objects.all()
    return render(request, "index.html", {'products': products})


def laptop(request):
    laptops = Laptop.objects.all()
    return render(request, "laptop.html", {"laptops": laptops})

def mobile(request):
    Mobiles = Mobile.objects.all()
    return render(request, "Mobile.html", {"Mobiles": Mobiles})


def watch_view(request):
    watchs = Watch.objects.all()
    return render(request, "watch.html", {"Watchs": watchs})

def book_view(request):
    books = Book.objects.all()
    return render(request,"book.html", {"Books": books})

def clothing_view(request):
    clothings = Clothing.objects.all()
    return render(request,"clothing.html", {"Clothings": clothings})


# Session key generator
def _get_session_key(request):
    if request.session.session_key:
        return request.session.session_key
    request.session.create()
    return request.session.session_key


# Add to Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = _get_session_key(request)
    cart_item = CartItem.objects.filter(session_key=session_key, product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(session_key=session_key, product=product, quantity=1)
    return redirect("view_cart")


# View Cart
def view_cart(request):
    session_key = _get_session_key(request)
    items = CartItem.objects.filter(session_key=session_key)
    total = sum([item.subtotal() for item in items])
    return render(request, "view_cart.html", {"items": items, "total": total})


# Update Cart
def update_cart(request, item_id):
    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))
        item = get_object_or_404(CartItem, id=item_id)
        if qty <= 0:
            item.delete()
        else:
            item.quantity = qty
            item.save()
    return redirect("view_cart")


# Remove from Cart
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("view_cart")


# Checkout
def checkout(request):
    session_key = _get_session_key(request)
    items = CartItem.objects.filter(session_key=session_key)
    if not items.exists():
        return redirect("homepage")

    total = sum([item.subtotal() for item in items])

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(
                name=data["name"],
                email=data["email"],
                phone=data.get("phone", ""),
                address=data.get("address", ""),
                total=total,
                status="Pending",
            )
            for it in items:
                OrderItem.objects.create(
                    order=order,
                    product=it.product,
                    quantity=it.quantity,
                    price=it.product.price
                )
            items.delete()
            return render(request, "checkout.html", {"order": order, "success": True})
    else:
        form = CheckoutForm()
    return render(request, "checkout.html", {"form": form, "items": items, "total": total})


# My Orders
@login_required
def my_orders(request):
    orders = Order.objects.filter(email=request.user.email).order_by("-created_at")
    return render(request, "order.html", {"orders": orders})


# ✅ User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "user_login.html")


# ✅ User Logout
def user_logout(request):
    logout(request)
    return redirect("homepage")


# ✅ Signup Form
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ✅ User Signup View
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            messages.success(request, "Signup successful! Welcome to MominKart.")
            return redirect("homepage")
    else:
        form = SignupForm()
    return render(request, "register.html", {"form": form})
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
