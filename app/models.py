from django.db import models


# =========================================================
# REGISTER
# =========================================================

class registerDB(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=150)

    def __str__(self):
        return self.Name


# =========================================================
# OTP
# =========================================================

class otp(models.Model):
    Email = models.EmailField()
    Otp = models.IntegerField()

    def __str__(self):
        return self.Email


# =========================================================
# PRODUCT
# =========================================================

class product(models.Model):
    Product_name = models.CharField(max_length=250)
    Vehichel_name = models.CharField(max_length=250)
    Category = models.CharField(max_length=250)
    Discription = models.CharField(max_length=2500)

    Price = models.CharField(max_length=250)
    Discount_price = models.CharField(max_length=250)

    Stock_availability = models.CharField(max_length=250)

    Warranty = models.CharField(max_length=250)
    Company = models.CharField(max_length=250)

    Brand_name = models.CharField(max_length=250)

    Image_url = models.CharField(max_length=5000)

    Short_discription = models.CharField(max_length=500)

    Brand = models.CharField(max_length=250)

    vehichel_brand = models.CharField(max_length=250)

    def __str__(self):
        return self.Product_name


# =========================================================
# CART
# =========================================================

class Cart(models.Model):
    User_email = models.CharField(max_length=250)
    product_id = models.CharField(max_length=250)

    def __str__(self):
            return self.User_email

class Favourite(models.Model):
    Email = models.EmailField()
    Product_id = models.IntegerField()

    def __str__(self):
            return self.Email

from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(
        registerDB,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True
    )

    mobile = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    pincode = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.Name