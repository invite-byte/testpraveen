from django.contrib import admin
from django.urls import path
from app import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # =====================================================
    # ADMIN
    # =====================================================

    path(
        'admin/',
        admin.site.urls
    ),


    # =====================================================
    # HOME
    # =====================================================

    path(
        'home/<str:name>',
        views.home,
        name='home'
    ),


    # =====================================================
    # LOGIN
    # =====================================================

    path(
        'login/',
        views.login,
        name='login'
    ),


    # =====================================================
    # REGISTER
    # =====================================================

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'registerSuccess/',
        views.registerSuccess,
        name='registerSuccess'
    ),


    # =====================================================
    # FORGOT PASSWORD
    # =====================================================

    path(
        'forget-password/',
        views.forgetPass,
        name='forgetPass'
    ),

    path(
        'forgetpassotp',
        views.forgetPassOTP,
        name='forgetpassotp'
    ),

    path(
        'createpass',
        views.createpass,
        name='createpass'
    ),


    # =====================================================
    # LANDING PAGE
    # =====================================================

    path(
        '',
        views.landingpage,
        name='landingpage'
    ),


    # =====================================================
    # CATEGORY PAGE
    # =====================================================

    path(
        '<str:name>/view-all-category',
        views.viewallcategory,
        name='viewallcategory'
    ),


    # =====================================================
    # ALL PRODUCTS
    #
    # IMPORTANT:
    # All filters will work through GET parameters.
    #
    # Example:
    #
    # /Praveen/All-product?category=Braking
    #
    # =====================================================

    path(
        '<str:name>/All-product',
        views.allproduct,
        name='allproduct'
    ),


    # =====================================================
    # INDIVIDUAL CATEGORY URLS
    # =====================================================

    path(
        '<str:name>/Charger',
        views.productcharger,
        name='productcharge'
    ),

    path(
        '<str:name>/Tyre',
        views.producttyre,
        name='producttyre'
    ),

    path(
        '<str:name>/Break-Pad',
        views.productbreak,
        name='productbreak'
    ),

    path(
        '<str:name>/Controller',
        views.productcontroller,
        name='productcontroller'
    ),

    path(
        '<str:name>/Motor',
        views.productmotor,
        name='productmotor'
    ),

    path(
        '<str:name>/Suspension',
        views.productsuspension,
        name='productsuspension'
    ),

    path(
        '<str:name>/Light',
        views.productlight,
        name='productlight'
    ),

    path(
        '<str:name>/Wires',
        views.productwire,
        name='productwiring'
    ),

    path(
        '<str:name>/Accessories',
        views.productaccessories,
        name='productaccessories'
    ),


    # =====================================================
    # CART
    # =====================================================

    path(
        'add-to-cart/<str:name>/<int:Product_id>/',
        views.addtocart,
        name='addtocart'
    ),

    path(
        '<str:name>/cart/',
        views.cart,
        name='cart'
    ),

    path(
        '<str:name>/remove-from-cart/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        '<str:name>/clear-cart/',
        views.clear_cart,
        name='clear_cart'
    ),

    path(
            '<str:name>/add-favourite/<int:product_id>/',
            views.add_favourite,
            name='add_favourite'
        ),

    path(
        '<str:name>/wishlist/',
        views.wishlist,
        name='wishlist'
    ),

    path(
        '<str:name>/remove-favourite/<int:product_id>/',
        views.remove_favourite,
        name='remove_favourite'
    ),

    path(
        'checkout/<str:name>/',
        views.checkout,
        name='checkout'
    ),

    path(
        'verify-checkout-otp/<str:name>/',
        views.verify_checkout_otp,
        name='verify_checkout_otp'
    ),

    path('profile/', views.profile, name='profile'),

    path('about/', views.about_view, name='about'),
]


# =========================================================
# MEDIA
# =========================================================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )