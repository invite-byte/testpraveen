from django import forms
from django.contrib import admin
from .models import product, otp, registerDB, Cart, Favourite, UserProfile


CATEGORY_CHOICES = [
    ('Braking Systems', 'Braking Systems'),
    ('Chargers & Charging', 'Chargers & Charging'),
    ('Tyres, Tubes & Wheels', 'Tyres, Tubes & Wheels'),
    ('Electrical & Controls', 'Electrical & Controls'),
    ('Motor & Drive Components', 'Motor & Drive Components'),
    ('Suspension', 'Suspension'),
    ('Lighting & Indicators', 'Lighting & Indicators'),
    ('Electrical Components', 'Electrical Components'),
    ('Accessories', 'Accessories'),
]


PRODUCT_BRAND_CHOICES = [
    ('EVoltParts', 'EVoltParts'),
    ('Ather', 'Ather'),
    ('Ola', 'Ola'),
    ('Bajaj', 'Bajaj'),
    ('TVS', 'TVS'),
    ('Vida', 'Vida'),
    ('Simple Energy', 'Simple Energy'),
]


VEHICLE_BRAND_CHOICES = [
    (
        'Universal - All Brands (Ather, Ola, TVS, Bajaj, Hero, Okinawa, etc.)',
        'Universal - All Brands (Ather, Ola, TVS, Bajaj, Hero, Okinawa, etc.)'
    ),
    ('Ather', 'Ather'),
    ('Ola', 'Ola'),
    ('Bajaj', 'Bajaj'),
    ('TVS', 'TVS'),
    ('Vida', 'Vida'),
    ('Simple Energy', 'Simple Energy'),
    ('Hero', 'Hero'),
    ('Okinawa', 'Okinawa'),
]

VEHICLE_NAME_CHOICES = [
    (
        'Universal - All EV Bikes & Scooters',
        'Universal - All EV Bikes & Scooters'
    ),

    # Ather
    ('Ather 450X', 'Ather 450X'),
    ('Ather 450S', 'Ather 450S'),
    ('Ather Rizta', 'Ather Rizta'),

    # Ola
    ('Ola S1 Pro', 'Ola S1 Pro'),
    ('Ola S1 Air', 'Ola S1 Air'),
    ('Ola S1X', 'Ola S1X'),

    # TVS
    ('TVS iQube', 'TVS iQube'),

    # Bajaj
    ('Bajaj Chetak', 'Bajaj Chetak'),

    # Vida
    ('Vida V1', 'Vida V1'),
    ('Vida V2', 'Vida V2'),

    # Simple Energy
    ('Simple One', 'Simple One'),

    # Hero Electric
    ('Hero Electric Optima', 'Hero Electric Optima'),

    # Okinawa
    ('Okinawa Praise', 'Okinawa Praise'),
    ('Okinawa Okhi90', 'Okinawa Okhi90'),
]


class ProductAdminForm(forms.ModelForm):

    Vehichel_name = forms.ChoiceField(
        choices=VEHICLE_NAME_CHOICES,
        label='Vehicle name',
    )

    Category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        label='Category',
    )

    Brand_name = forms.ChoiceField(
        choices=PRODUCT_BRAND_CHOICES,
        label='Product Brand',
    )

    vehichel_brand = forms.ChoiceField(
        choices=VEHICLE_BRAND_CHOICES,
        label='Vehicle Brand',
    )

    class Meta:
        model = product
        fields = '__all__'

@admin.register(product)
class ProductAdmin(admin.ModelAdmin):

    form = ProductAdminForm

    list_display = (
        'Product_name',
        'Category',
        'Brand_name',
        'vehichel_brand',
        'Price',
        'Discount_price',
        'Stock_availability',
    )

    list_filter = (
        'Category',
        'Brand_name',
        'vehichel_brand',
        'Stock_availability',
    )

    search_fields = (
        'Product_name',
        'Vehichel_name',
        'Brand_name',
    )

    fieldsets = (
        ('Product Details', {
            'fields': (
                'Product_name',
                'Vehichel_name',
                'Category',
            )
        }),

        ('Description', {
            'fields': (
                'Short_discription',
                'Discription',
            )
        }),

        ('Pricing & Stock', {
            'fields': (
                'Price',
                'Discount_price',
                'Stock_availability',
                'Warranty',
            )
        }),

        ('Brand Details', {
            'fields': (
                'Brand_name',
                'vehichel_brand',
                'Company',
                'Brand',
            )
        }),

        ('Media', {
            'fields': (
                'Image_url',
            )
        }),
    )


admin.site.register(registerDB)
admin.site.register(otp)
admin.site.register(Cart)
admin.site.register(Favourite)
admin.site.register(UserProfile)