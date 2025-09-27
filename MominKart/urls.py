from django.contrib import admin
from django.urls import path
from MominKart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main Pages
    path('', views.homepage, name='homepage'),
    path('laptop/', views.laptop, name='laptop'),
    path('watch_view/', views.watch_view, name='watch'),
    path('mobile/',views.mobile,name="Mobile"),
    path('watch/', views.watch_view, name='watch'),
    path('book/', views.book_view, name='book'),
    path('clothing/', views.clothing_view, name='clothing'),
    # Auth
    path('user_login/', views.user_login, name='login'),
    path('user_logout/', views.user_logout, name='logout'),

    # Cart & Orders
    path('view_cart/', views.view_cart, name='view_cart'),   # ✅ fixed
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("update-cart/<int:item_id>/", views.update_cart, name="update_cart"),
    path("remove-item/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("orders/", views.my_orders, name="my_orders"),
    path("signup/", views.user_signup, name="user_signup"),
    path("register/", views.user_signup, name="register"),
    path('profile/', views.profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
