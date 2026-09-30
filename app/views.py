from django.shortcuts import render, redirect
from .models import registerDB, otp, product, Cart, Favourite, UserProfile
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
from random import randint
from django.db.models import Q


# =========================================================
# LOGIN
# =========================================================

def login(req):

    if req.method == 'POST':

        email = req.POST.get('email')
        password = req.POST.get('password')

        user_data = registerDB.objects.filter(
            Email=email
        )

        if not user_data.exists():

            return render(
                req,
                'login.html',
                {
                    'errormsg':
                        'Entered Mail is Not Registered...'
                }
            )

        user = user_data.first()

        if check_password(password, user.Password):

            # Store login information in session
            req.session['email'] = user.Email
            req.session['name'] = user.Name

            return redirect(
                'home',
                name=user.Name
            )

        else:

            return render(
                req,
                'login.html',
                {
                    'errormsg':
                        'Password is Incorrect...'
                }
            )

    return render(
        req,
        'login.html'
    )


# =========================================================
# HOME
# =========================================================

def home(req, name):

    return render(
        req,
        'home.html',
        {
            'name': name
        }
    )


# =========================================================
# REGISTER SUCCESS
# =========================================================

def registerSuccess(req):

    return render(
        req,
        'registerSuccess.html'
    )


# =========================================================
# REGISTER
# =========================================================

def register(req):

    if req.method == 'POST':

        name = req.POST.get('fullname')
        mobile = req.POST.get('mobile')
        email = req.POST.get('email')
        password = req.POST.get('password')
        con_password = req.POST.get('confirm_password')

        # ---------------------------------------------
        # Password validation
        # ---------------------------------------------

        if password != con_password:

            return render(
                req,
                'register.html',
                {
                    'message':
                        'Passwords do not match.'
                }
            )

        # ---------------------------------------------
        # Email validation
        # ---------------------------------------------

        all_email = registerDB.objects.filter(
            Email=email
        )

        if all_email.exists():

            return render(
                req,
                'register.html',
                {
                    'message':
                        'Entered Email is Already Taken'
                }
            )

        # ---------------------------------------------
        # Hash password
        # ---------------------------------------------

        password = make_password(password)

        # ---------------------------------------------
        # Create user
        # ---------------------------------------------

        obj = registerDB(
            Name=name,
            Mobile=mobile,
            Email=email,
            Password=password
        )

        obj.save()

        return redirect(
            '/registerSuccess'
        )

    return render(
        req,
        'register.html'
    )


# =========================================================
# FORGOT PASSWORD
# =========================================================

def forgetPass(req):

    if req.method == 'POST':

        email = req.POST.get('email')

        all_email = registerDB.objects.filter(
            Email=email
        )

        if all_email.exists():

            sender = settings.EMAIL_HOST_USER

            subject = "eBikeMart Password Reset"

            random_num = randint(
                100000,
                999999
            )

            # ---------------------------------------------
            # Update existing OTP or create new OTP
            # ---------------------------------------------

            email_check = otp.objects.filter(
                Email=email
            ).first()

            if email_check:

                email_check.Otp = random_num
                email_check.save()

            else:

                otp.objects.create(
                    Email=email,
                    Otp=random_num
                )

            message = (
                "Your verification code is.........."
                + str(random_num)
                + ".........."
            )

            send_mail(
                subject,
                message,
                sender,
                [email]
            )

            return render(
                req,
                'forgetpassotp.html',
                {
                    'email': email
                }
            )

        else:

            return render(
                req,
                'forgetpass.html',
                {
                    'message':
                        'Entered email is not registered.'
                }
            )

    return render(
        req,
        'forgetpass.html'
    )


# =========================================================
# FORGOT PASSWORD OTP
# =========================================================

def forgetPassOTP(req):

    if req.method == 'POST':

        email = req.POST.get('email')

        user_otp = req.POST.get(
            'verification_code'
        )

        # ---------------------------------------------
        # Email missing
        # ---------------------------------------------

        if not email:

            return render(
                req,
                'forgetpass.html',
                {
                    'message':
                        'Email is missing. Please try again.'
                }
            )

        # ---------------------------------------------
        # OTP missing
        # ---------------------------------------------

        if not user_otp:

            return render(
                req,
                'forgetpassotp.html',
                {
                    'email': email,
                    'errormsg':
                        'Please enter the OTP.'
                }
            )

        # ---------------------------------------------
        # Find OTP
        # ---------------------------------------------

        otp_data = otp.objects.filter(
            Email=email
        ).first()

        if otp_data is None:

            return render(
                req,
                'forgetpass.html',
                {
                    'message':
                        'OTP not found. Please request a new OTP.'
                }
            )

        # ---------------------------------------------
        # Compare OTP
        # ---------------------------------------------

        if str(user_otp) == str(otp_data.Otp):

            return render(
                req,
                'createpass.html',
                {
                    'email': email
                }
            )

        else:

            return render(
                req,
                'forgetpassotp.html',
                {
                    'email': email,
                    'errormsg':
                        'Incorrect OTP. Please try again.'
                }
            )

    return render(
        req,
        'forgetpassotp.html'
    )


# =========================================================
# CREATE PASSWORD
# =========================================================

def createpass(req):

    if req.method == 'POST':

        one = req.POST.get('first-pass')
        two = req.POST.get('second-pass')
        email = req.POST.get('email')

        if one == two:

            get_det = registerDB.objects.filter(
                Email=email
            ).first()

            if get_det is None:

                return render(
                    req,
                    'createpass.html',
                    {
                        'passerrormsg':
                            'Email is not registered.'
                    }
                )

            get_det.Password = make_password(two)

            get_det.save()

            return render(
                req,
                'passchangedsuccess.html'
            )

        else:

            return render(
                req,
                'createpass.html',
                {
                    'email': email,
                    'passerrormsg':
                        'Password Must be Same...'
                }
            )

    return render(
        req,
        'createpass.html'
    )


# =========================================================
# PASSWORD CHANGED SUCCESS
# =========================================================

def createpasssuccess(req):

    return render(
        req,
        'passchangedsuccess.html'
    )


# =========================================================
# LANDING PAGE
# =========================================================

def landingpage(req):

    return render(
        req,
        'index.html'
    )


# =========================================================
# VIEW ALL CATEGORY
# =========================================================

def viewallcategory(req, name):

    return render(
        req,
        'viewallcategory.html',
        {
            'name': name
        }
    )


# =========================================================
# ALL PRODUCTS
# =========================================================

# =========================================================
# ALL PRODUCTS
# =========================================================

def allproduct(req, name):

    # =====================================================
    # START WITH ALL PRODUCTS
    # =====================================================

    details = product.objects.all()


    # =====================================================
    # SEARCH
    # =====================================================

    search = req.GET.get('q', '').strip()

    if search:

        details = details.filter(

            Q(Product_name__icontains=search) |

            Q(Vehichel_name__icontains=search) |

            Q(Category__icontains=search) |

            Q(Brand_name__icontains=search) |

            Q(vehichel_brand__icontains=search) |

            Q(Brand__icontains=search) |

            Q(Company__icontains=search) |

            Q(Short_discription__icontains=search) |

            Q(Discription__icontains=search)

        )


    # =====================================================
    # CATEGORY FILTER
    # =====================================================
    #
    # HTML sends:
    #
    # braking
    # electrical
    # charging
    # motor
    # tyres
    # lighting
    # suspension
    # wires
    # accessories
    #
    # Database contains values such as:
    #
    # Braking Systems
    # Chargers & Charging
    # Tyres, Tubes & Wheels
    # Electrical & Controls
    # Motor & Drive Components
    # Suspension
    # Lighting & Indicators
    # Electrical Components
    # Accessories
    #
    # =====================================================

    category = req.GET.get(
        'category',
        ''
    ).strip().lower()


    if category:

        # -------------------------------------------------
        # BRAKING
        # -------------------------------------------------

        if category == 'braking':

            details = details.filter(

                Q(Category__icontains='brake') |

                Q(Category__icontains='braking') |

                Q(Category__icontains='break')

            )


        # -------------------------------------------------
        # ELECTRICAL
        # -------------------------------------------------

        elif category == 'electrical':

            details = details.filter(

                Q(Category__icontains='electrical') |

                Q(Category__icontains='controller') |

                Q(Category__icontains='control')

            )


        # -------------------------------------------------
        # CHARGING
        # -------------------------------------------------

        elif category == 'charging':

            details = details.filter(

                Q(Category__icontains='charger') |

                Q(Category__icontains='charging')

            )


        # -------------------------------------------------
        # MOTOR
        # -------------------------------------------------

        elif category == 'motor':

            details = details.filter(

                Q(Category__icontains='motor') |

                Q(Category__icontains='drive')

            )


        # -------------------------------------------------
        # TYRES
        # -------------------------------------------------

        elif category == 'tyres':

            details = details.filter(

                Q(Category__icontains='tyre') |

                Q(Category__icontains='tire') |

                Q(Category__icontains='wheel') |

                Q(Category__icontains='tube')

            )


        # -------------------------------------------------
        # LIGHTING
        # -------------------------------------------------

        elif category == 'lighting':

            details = details.filter(

                Q(Category__icontains='light') |

                Q(Category__icontains='lighting') |

                Q(Category__icontains='indicator')

            )


        # -------------------------------------------------
        # SUSPENSION
        # -------------------------------------------------

        elif category == 'suspension':

            details = details.filter(

                Q(Category__icontains='suspension')

            )


        # -------------------------------------------------
        # WIRING
        # -------------------------------------------------

        elif category == 'wires':

            details = details.filter(

                Q(Category__icontains='wire') |

                Q(Category__icontains='wiring') |

                Q(Category__icontains='cable')

            )


        # -------------------------------------------------
        # ACCESSORIES
        # -------------------------------------------------

        elif category == 'accessories':

            details = details.filter(

                Q(Category__icontains='accessor')

            )


    # =====================================================
    # VEHICLE BRAND FILTER
    # =====================================================
    #
    # IMPORTANT:
    #
    # Vehicle Brand is stored in:
    #
    #     vehichel_brand
    #
    # NOT:
    #
    #     Brand
    #
    # =====================================================

    vehicle_brand = req.GET.get(
        'vehicle_brand',
        ''
    ).strip()


    if vehicle_brand:

        details = details.filter(

            vehichel_brand__icontains=vehicle_brand

        )


    # =====================================================
    # VEHICLE MODEL FILTER
    # =====================================================
    #
    # HTML example:
    #
    # value="450X"
    #
    # Database example:
    #
    # Ather 450X
    #
    # Therefore icontains is intentionally used.
    #
    # =====================================================

    vehicle_name = req.GET.get(
        'vehicle_name',
        ''
    ).strip()


    if vehicle_name:

        details = details.filter(

            Vehichel_name__icontains=vehicle_name

        )


    # =====================================================
    # PRODUCT BRAND FILTER
    # =====================================================
    #
    # Product Brand is:
    #
    # Brand_name
    #
    # =====================================================

    product_brand = req.GET.get(
        'product_brand',
        ''
    ).strip()


    if product_brand:

        details = details.filter(

            Brand_name__icontains=product_brand

        )


    # =====================================================
    # COMPANY FILTER
    # =====================================================

    company = req.GET.get(
        'company',
        ''
    ).strip()


    if company:

        details = details.filter(

            Company__icontains=company

        )


    # =====================================================
    # STOCK FILTER
    # =====================================================
    #
    # IMPORTANT:
    #
    # Do NOT use:
    #
    # Stock_availability__icontains='available'
    #
    # for "In Stock", because "unavailable" also contains
    # the word "available".
    #
    # =====================================================

    stock = req.GET.get(
        'stock',
        ''
    ).strip().lower()


    if stock:

        # -------------------------------------------------
        # IN STOCK
        # -------------------------------------------------

        if stock == 'available':

            details = details.filter(

                Q(
                    Stock_availability__iexact='available'
                ) |

                Q(
                    Stock_availability__iexact='in stock'
                ) |

                Q(
                    Stock_availability__iexact='instock'
                ) |

                Q(
                    Stock_availability__iexact='yes'
                )

            )


        # -------------------------------------------------
        # OUT OF STOCK
        # -------------------------------------------------

        elif stock == 'out':

            details = details.filter(

                Q(
                    Stock_availability__iexact='out'
                ) |

                Q(
                    Stock_availability__iexact='out of stock'
                ) |

                Q(
                    Stock_availability__iexact='outofstock'
                ) |

                Q(
                    Stock_availability__iexact='unavailable'
                ) |

                Q(
                    Stock_availability__iexact='no'
                )

            )


    # =====================================================
    # NAVBAR BRAND FILTER
    # =====================================================
    #
    # This is kept separately from the Product Brand filter
    # because your existing navbar may send ?brand=...
    #
    # =====================================================

    selected_brand = req.GET.get(
        'brand',
        ''
    ).strip()


    if selected_brand:

        details = details.filter(

            Brand__icontains=selected_brand

        )


    # =====================================================
    # SORTING
    # =====================================================

    sort = req.GET.get(
        'sort',
        ''
    ).strip()


    # -----------------------------------------------------
    # NAME A TO Z
    # -----------------------------------------------------

    if sort == 'name_asc':

        details = details.order_by(
            'Product_name'
        )


    # -----------------------------------------------------
    # NAME Z TO A
    # -----------------------------------------------------

    elif sort == 'name_desc':

        details = details.order_by(
            '-Product_name'
        )


    # -----------------------------------------------------
    # NEWEST
    # -----------------------------------------------------

    elif sort == 'newest':

        details = details.order_by(
            '-id'
        )


    # -----------------------------------------------------
    # OLDEST
    # -----------------------------------------------------

    elif sort == 'oldest':

        details = details.order_by(
            'id'
        )


    # -----------------------------------------------------
    # PRICE LOW TO HIGH
    # -----------------------------------------------------
    #
    # Price is currently CharField in your model, so Django
    # cannot directly sort it numerically.
    #
    # Therefore convert the queryset to a list and use the
    # existing get_price_value() helper.
    #
    # -----------------------------------------------------

    elif sort == 'price_low':

        details = list(details)

        details.sort(

            key=lambda item:

                get_price_value(

                    item.Discount_price

                    if item.Discount_price

                    else item.Price

                )

        )


    # -----------------------------------------------------
    # PRICE HIGH TO LOW
    # -----------------------------------------------------

    elif sort == 'price_high':

        details = list(details)

        details.sort(

            key=lambda item:

                get_price_value(

                    item.Discount_price

                    if item.Discount_price

                    else item.Price

                ),

            reverse=True

        )


    # =====================================================
    # DYNAMIC PRODUCT BRANDS
    # =====================================================

    product_brands = product.objects.values_list(

        'Brand_name',

        flat=True

    ).distinct().order_by(

        'Brand_name'

    )


    # =====================================================
    # DYNAMIC VEHICLE BRANDS
    # =====================================================

    vehicle_brands = product.objects.values_list(

        'vehichel_brand',

        flat=True

    ).distinct().order_by(

        'vehichel_brand'

    )


    # =====================================================
    # USER INFORMATION
    # =====================================================

    email = req.session.get(
        'email'
    )


    favorite_product_ids = []

    favorite_count = 0

    cart_count = 0


    if email:

        # -------------------------------------------------
        # FAVOURITES
        # -------------------------------------------------

        favorite_product_ids = list(

            Favourite.objects.filter(

                Email=email

            ).values_list(

                'Product_id',

                flat=True

            )

        )


        favorite_count = len(
            favorite_product_ids
        )


        # -------------------------------------------------
        # CART
        # -------------------------------------------------

        cart_count = Cart.objects.filter(

            User_email=email

        ).count()


    # =====================================================
    # RETURN PAGE
    # =====================================================

    return render(

        req,

        'allproduct.html',

        {

            # -------------------------------------------------
            # USER
            # -------------------------------------------------

            'name':
                name,


            # -------------------------------------------------
            # PRODUCTS
            # -------------------------------------------------

            'Datas':
                details,


            # -------------------------------------------------
            # SEARCH
            # -------------------------------------------------

            'search_query':
                search,


            # -------------------------------------------------
            # SELECTED FILTERS
            # -------------------------------------------------

            'selected_category':
                category,

            'selected_vehicle_brand':
                vehicle_brand,

            'selected_vehicle_name':
                vehicle_name,

            'selected_product_brand':
                product_brand,

            'selected_company':
                company,

            'selected_stock':
                stock,

            'selected_sort':
                sort,

            'selected_brand':
                selected_brand,


            # -------------------------------------------------
            # FILTER OPTIONS
            # -------------------------------------------------

            'product_brands':
                product_brands,

            'vehicle_brands':
                vehicle_brands,


            # -------------------------------------------------
            # FAVOURITES
            # -------------------------------------------------

            'favorite_product_ids':
                favorite_product_ids,

            'favorite_count':
                favorite_count,


            # -------------------------------------------------
            # CART
            # -------------------------------------------------

            'cart_count':
                cart_count,

        }

    )

def get_price_value(price):

    if not price:

        return 0

    try:

        price_text = str(price)

        price_text = (
            price_text
            .replace('₹', '')
            .replace(',', '')
            .replace('Rs.', '')
            .replace('Rs', '')
            .strip()
        )

        return float(price_text)

    except (
        ValueError,
        TypeError
    ):

        return 0


# =========================================================
# CHARGER PRODUCTS
# =========================================================

def productcharger(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Charger') |
        Q(Category__icontains='Chargers') |
        Q(Category__icontains='Charging')

    )

    return render(
        req,
        'productcharger.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# TYRE PRODUCTS
# =========================================================

def producttyre(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Tyre') |
        Q(Category__icontains='Tyres')

    )

    return render(
        req,
        'producttyre.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# BRAKE PRODUCTS
# =========================================================

def productbreak(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Brake') |
        Q(Category__icontains='Break-Pad') |
        Q(Category__icontains='Braking Systems')

    )

    return render(
        req,
        'productbreak.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# CONTROLLER PRODUCTS
# =========================================================

def productcontroller(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Controller') |
        Q(Category__icontains='Controls')

    )

    return render(
        req,
        'productcontroller.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# MOTOR PRODUCTS
# =========================================================

def productmotor(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Motor') |
        Q(Category__icontains='Motors')

    )

    return render(
        req,
        'productmotor.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# SUSPENSION PRODUCTS
# =========================================================

def productsuspension(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Suspension') |
        Q(Category__icontains='Suspensions')

    )

    return render(
        req,
        'productsuspension.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# LIGHT PRODUCTS
# =========================================================

def productlight(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Light') |
        Q(Category__icontains='Indicator') |
        Q(Category__icontains='Indicators')

    )

    return render(
        req,
        'productlight.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# WIRING PRODUCTS
# =========================================================

def productwire(req, name):

    final_details = product.objects.filter(

        Q(Category__icontains='Cable') |
        Q(Category__icontains='Wire') |
        Q(Category__icontains='Electrical Components')

    )

    return render(
        req,
        'productwire.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# ACCESSORIES
# =========================================================

def productaccessories(req, name):

    final_details = product.objects.filter(

        Category__icontains='Accessories'

    )

    return render(
        req,
        'productaccessories.html',
        {
            'name': name,
            'Datas': final_details
        }
    )


# =========================================================
# ADD TO CART
# =========================================================

def addtocart(req, name, Product_id):

    # ---------------------------------------------
    # Get logged-in user email
    # ---------------------------------------------

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    # ---------------------------------------------
    # Check product
    # ---------------------------------------------

    selected_product = product.objects.filter(
        id=Product_id
    ).first()

    if selected_product is None:

        return redirect(
            'allproduct',
            name=name
        )


    # ---------------------------------------------
    # Check duplicate cart item
    # ---------------------------------------------

    already_in_cart = Cart.objects.filter(

        User_email=email,

        product_id=Product_id

    ).exists()


    # ---------------------------------------------
    # Add product
    # ---------------------------------------------

    if not already_in_cart:

        Cart.objects.create(

            User_email=email,

            product_id=Product_id

        )


    # ---------------------------------------------
    # Open cart
    # ---------------------------------------------

    return redirect(
        'cart',
        name=name
    )


# =========================================================
# CART
# =========================================================

def cart(req, name):

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    # ---------------------------------------------
    # User's cart
    # ---------------------------------------------

    product_cart = Cart.objects.filter(
        User_email=email
    )


    all_product_cart = []

    total_amount = 0

    total_discount_amount = 0


    # ---------------------------------------------
    # Get products
    # ---------------------------------------------

    for item in product_cart:

        selected_product = product.objects.filter(
            id=item.product_id
        ).first()


        # Product deleted from database
        if selected_product is None:

            continue


        # -----------------------------------------
        # Original price
        # -----------------------------------------

        price = get_price_value(
            selected_product.Price
        )


        # -----------------------------------------
        # Discount price
        # -----------------------------------------

        if selected_product.Discount_price:

            discount_price = get_price_value(
                selected_product.Discount_price
            )

        else:

            discount_price = price


        # -----------------------------------------
        # Calculate totals
        # -----------------------------------------

        total_amount += price

        total_discount_amount += discount_price


        all_product_cart.append(
            selected_product
        )


    # ---------------------------------------------
    # Discount
    # ---------------------------------------------

    discount = (
        total_amount -
        total_discount_amount
    )


    # ---------------------------------------------
    # Final total
    # ---------------------------------------------

    final_total = total_discount_amount


    return render(
        req,
        'addtocart.html',
        {

            'cart':
                all_product_cart,

            'sub_total_amount':
                total_amount,

            'discount':
                discount,

            'total_amount':
                final_total,

            'name':
                name,

            'cart_count':
                len(all_product_cart)

        }
    )


# =========================================================
# REMOVE ONE PRODUCT FROM CART
# =========================================================

def remove_from_cart(req, name, product_id):

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    Cart.objects.filter(

        User_email=email,

        product_id=product_id

    ).delete()


    return redirect(
        'cart',
        name=name
    )


# =========================================================
# CLEAR ENTIRE CART
# =========================================================

def clear_cart(req, name):

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    Cart.objects.filter(
        User_email=email
    ).delete()


    return redirect(
        'cart',
        name=name
    )


# =========================================================
# TOGGLE FAVOURITE
# =========================================================
#
# Click once  -> Add favourite
# Click again -> Remove favourite
#
# =========================================================

def toggle_favourite(req, name, product_id):

    email = req.session.get(
        'email'
    )

    # ---------------------------------------------
    # Login check
    # ---------------------------------------------

    if not email:

        return redirect('/login')


    # ---------------------------------------------
    # Check product
    # ---------------------------------------------

    selected_product = product.objects.filter(
        id=product_id
    ).first()

    if selected_product is None:

        return redirect(
            'allproduct',
            name=name
        )


    # ---------------------------------------------
    # Find existing favourite
    # ---------------------------------------------

    favourite = Favourite.objects.filter(

        Email=email,

        Product_id=product_id

    ).first()


    # ---------------------------------------------
    # Already favourite -> REMOVE
    # ---------------------------------------------

    if favourite:

        favourite.delete()


    # ---------------------------------------------
    # Not favourite -> ADD
    # ---------------------------------------------

    else:

        Favourite.objects.create(

            Email=email,

            Product_id=product_id

        )


    # ---------------------------------------------
    # Return to product page
    # ---------------------------------------------

    return redirect(
        'allproduct',
        name=name
    )


# =========================================================
# ADD FAVOURITE
# =========================================================
#
# Kept for compatibility with any old template/URL
# that still calls add_favourite.
#
# =========================================================

def add_favourite(req, name, product_id):

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    selected_product = product.objects.filter(
        id=product_id
    ).first()

    if selected_product is None:

        return redirect(
            'allproduct',
            name=name
        )


    already_exists = Favourite.objects.filter(

        Email=email,

        Product_id=product_id

    ).exists()


    if not already_exists:

        Favourite.objects.create(

            Email=email,

            Product_id=product_id

        )


    return redirect(
        'allproduct',
        name=name
    )


# =========================================================
# WISHLIST
# =========================================================

def wishlist(req, name):

    # ---------------------------------------------
    # Get logged-in user's email
    # ---------------------------------------------

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    # ---------------------------------------------
    # Get only this user's favourites
    # ---------------------------------------------

    favourite_records = Favourite.objects.filter(
        Email=email
    )


    # ---------------------------------------------
    # Get product IDs
    # ---------------------------------------------

    product_ids = favourite_records.values_list(
        'Product_id',
        flat=True
    )


    # ---------------------------------------------
    # Get actual product objects
    # ---------------------------------------------

    wishlist_items = product.objects.filter(
        id__in=product_ids
    )


    # ---------------------------------------------
    # Cart count
    # ---------------------------------------------

    cart_count = Cart.objects.filter(
        User_email=email
    ).count()


    # ---------------------------------------------
    # Favourite count
    # ---------------------------------------------

    favorite_count = favourite_records.count()


    # ---------------------------------------------
    # Render wishlist
    # ---------------------------------------------

    return render(
        req,
        'favourite.html',
        {

            'name':
                name,

            'wishlist_items':
                wishlist_items,

            'favorite_count':
                favorite_count,

            'cart_count':
                cart_count

        }
    )


# =========================================================
# REMOVE FAVOURITE
# =========================================================

def remove_favourite(req, name, product_id):

    email = req.session.get(
        'email'
    )

    if not email:

        return redirect('/login')


    # ---------------------------------------------
    # Remove ONLY this user's favourite
    # ---------------------------------------------

    Favourite.objects.filter(

        Email=email,

        Product_id=product_id

    ).delete()


    # ---------------------------------------------
    # Return to wishlist
    # ---------------------------------------------

    return redirect(
        'wishlist',
        name=name
    )


# =========================================================
# CHECKOUT
# =========================================================

def checkout(req, name):

    # -----------------------------------------------------
    # Get logged-in user's email
    # -----------------------------------------------------

    email = req.session.get('email')

    if not email:

        return redirect('/login')


    # -----------------------------------------------------
    # Check whether cart contains products
    # -----------------------------------------------------

    cart_items = Cart.objects.filter(
        User_email=email
    )

    if not cart_items.exists():

        return redirect(
            'cart',
            name=name
        )


    # -----------------------------------------------------
    # Get registered user
    # -----------------------------------------------------

    user = registerDB.objects.filter(
        Email=email
    ).first()

    if user is None:

        return redirect('/login')


    # -----------------------------------------------------
    # Generate random 6 digit OTP
    # -----------------------------------------------------

    random_num = randint(
        100000,
        999999
    )


    # -----------------------------------------------------
    # Store OTP in session
    # -----------------------------------------------------

    req.session['checkout_otp'] = str(
        random_num
    )

    req.session['checkout_email'] = email


    # -----------------------------------------------------
    # Send OTP to registered email
    # -----------------------------------------------------

    subject = "EVoltParts Order Verification OTP"

    message = (
        "Hello "
        + user.Name
        + ",\n\n"

        "Your EVoltParts order verification OTP is:\n\n"

        + str(random_num)
        + "\n\n"

        "Please enter this OTP on the checkout page "
        "to confirm your order.\n\n"

        "This OTP is valid for this checkout session only.\n\n"

        "Thank you for shopping with EVoltParts."
    )


    sender = settings.EMAIL_HOST_USER


    send_mail(
        subject,
        message,
        sender,
        [email]
    )


    # -----------------------------------------------------
    # Open OTP page
    # -----------------------------------------------------

    return render(
        req,
        'checkout.html',
        {
            'name': name,
            'email': email
        }
    )


# =========================================================
# VERIFY CHECKOUT OTP
# =========================================================

def verify_checkout_otp(req, name):

    # -----------------------------------------------------
    # Login check
    # -----------------------------------------------------

    email = req.session.get('email')

    if not email:

        return redirect('/login')


    # -----------------------------------------------------
    # Only POST allowed
    # -----------------------------------------------------

    if req.method == 'POST':

        entered_otp = req.POST.get(
            'verification_code'
        )


        # -------------------------------------------------
        # Get stored OTP
        # -------------------------------------------------

        stored_otp = req.session.get(
            'checkout_otp'
        )

        stored_email = req.session.get(
            'checkout_email'
        )


        # -------------------------------------------------
        # OTP missing
        # -------------------------------------------------

        if not entered_otp:

            return render(
                req,
                'checkout.html',
                {
                    'name': name,
                    'email': email,
                    'errormsg':
                        'Please enter the OTP.'
                }
            )


        # -------------------------------------------------
        # OTP/session missing
        # -------------------------------------------------

        if not stored_otp or not stored_email:

            return render(
                req,
                'checkout.html',
                {
                    'name': name,
                    'email': email,
                    'errormsg':
                        'OTP expired. Please try checkout again.'
                }
            )


        # -------------------------------------------------
        # Check email
        # -------------------------------------------------

        if stored_email != email:

            return render(
                req,
                'checkout.html',
                {
                    'name': name,
                    'email': email,
                    'errormsg':
                        'Invalid checkout session.'
                }
            )


        # -------------------------------------------------
        # Verify OTP
        # -------------------------------------------------

        if str(entered_otp).strip() == str(stored_otp).strip():

            # ---------------------------------------------
            # OTP correct
            # ---------------------------------------------

            # Remove OTP from session
            req.session.pop(
                'checkout_otp',
                None
            )

            req.session.pop(
                'checkout_email',
                None
            )


            # ---------------------------------------------
            # Clear cart after successful order
            # ---------------------------------------------

            Cart.objects.filter(
                User_email=email
            ).delete()


            # ---------------------------------------------
            # Show order success page
            # ---------------------------------------------

            return render(
                req,
                'ordersuccess.html',
                {
                    'name': name
                }
            )


        else:

            # ---------------------------------------------
            # Incorrect OTP
            # ---------------------------------------------

            return render(
                req,
                'checkout.html',
                {
                    'name': name,
                    'email': email,
                    'errormsg':
                        'Incorrect OTP. Please try again.'
                }
            )


    # -----------------------------------------------------
    # GET request
    # -----------------------------------------------------

    return render(
        req,
        'checkout.html',
        {
            'name': name,
            'email': email
        }
    )

def profile(req):

    email = req.session.get('email')

    # User is not logged in
    if not email:
        return redirect('login')

    # Get logged-in user
    user = registerDB.objects.get(Email=email)

    # Create profile if it doesn't exist
    user_profile, created = UserProfile.objects.get_or_create(
        user=user
    )

    if req.method == 'POST':

        # -----------------------------
        # UPDATE NAME
        # -----------------------------

        name = req.POST.get('name')

        if name:
            user.Name = name


        # -----------------------------
        # UPDATE MOBILE
        # -----------------------------

        user_profile.mobile = req.POST.get('mobile')


        # -----------------------------
        # UPDATE DATE OF BIRTH
        # -----------------------------

        user_profile.date_of_birth = (
            req.POST.get('date_of_birth') or None
        )


        # -----------------------------
        # UPDATE ADDRESS
        # -----------------------------

        user_profile.address = req.POST.get('address')


        # -----------------------------
        # UPDATE CITY
        # -----------------------------

        user_profile.city = req.POST.get('city')


        # -----------------------------
        # UPDATE STATE
        # -----------------------------

        user_profile.state = req.POST.get('state')


        # -----------------------------
        # UPDATE PINCODE
        # -----------------------------

        user_profile.pincode = req.POST.get('pincode')


        # -----------------------------
        # UPDATE PROFILE PHOTO
        # -----------------------------

        if req.FILES.get('profile_photo'):

            user_profile.profile_photo = req.FILES.get(
                'profile_photo'
            )


        # -----------------------------
        # SAVE EVERYTHING
        # -----------------------------

        user.save()
        user_profile.save()


        # Update session name
        req.session['name'] = user.Name


        # -----------------------------
        # SHOW SUCCESS POPUP
        # -----------------------------

        return render(
            req,
            'profile.html',
            {
                'user': user,
                'profile': user_profile,
                'profile_updated': True
            }
        )


    # Normal GET request

    return render(
        req,
        'profile.html',
        {
            'user': user,
            'profile': user_profile
        }
    )

def about_view(req):

    name = req.session.get('name')

    return render(
        req,
        'about.html',
        {
            'name': name
        }
    )