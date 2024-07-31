from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime

# local imports
from .models import *
from .utils import cartData

from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.conf import settings

# Shop Home
def home(request):
    
    data = cartData(request)

    products = Product.objects.all() # all the products
    cartItems = data['cartItems'] # cart item count
    items = data['items'] # Items in Cart
    
    context = {
        'products': products,
        'cartItems': cartItems,
        'items': items,
    }
    return render(request, 'shop/index.html', context=context)

# Shop About :- /tss/about
def Banking(request):
    return render(request, 'shop/Banking.html')
    
# Shop About :- /tss/about
def careers(request):
    return render(request, 'shop/careers.html')

# Shop About :- /tss/about
def Website_development(request):
    return render(request, 'shop/Website_development.html')

# Shop About :- /tss/about
def developers_and_property_managers(request):
    return render(request, 'shop/developers_and_property_managers.html')

# Shop About :- /tss/about
def energy_and_resources_industry(request):
    return render(request, 'shop/energy_and_resources_industry.html')

# Shop About :- /tss/about
def retail_and_banking(request):
    return render(request, 'shop/retail_and_banking.html')

# Shop About :- /tss/about
def general_contractors_program_and_construction_managers(request):
    return render(request, 'shop/general_contractors_program_and_construction_managers.html')

# Shop About :- /tss/about
def Transportation(request):
    return render(request, 'shop/Transportation.html')

# Shop About :- /tss/about
def manufacturing_and_technology_industry(request):
    return render(request, 'shop/manufacturing_and_technology_industry.html')

# Shop About :- /tss/about
def Healthcare(request):
    return render(request, 'shop/Healthcare.html')

# Shop About :- /tss/about
def education(request):
    return render(request, 'shop/education.html')

# Shop About :- /tss/about
def engineering_design_and_consulting(request):
    return render(request, 'shop/engineering_design_and_consulting.html')

# Shop About :- /tss/about
def government(request):
    return render(request, 'shop/government.html')
    
# Shop About :- /tss/about
def hospitality_industry(request):
    return render(request, 'shop/hospitality_industry.html')
    
# Shop About :- /tss/about
def Product_Overview(request):
    return render(request, 'shop/Product_Overview.html')
    
# Shop About :- /tss/about
def Funds(request):
    return render(request, 'shop/Funds.html')
    
# Shop About :- /tss/about
def Insurance(request):
    return render(request, 'shop/Insurance.html')
    
# Shop About :- /tss/about
def Pensions(request):
    return render(request, 'shop/Pensions.html')
    
# Shop About :- /tss/about
def Wealth_Management(request):
    return render(request, 'shop/Wealth_Management.html')
    
# Shop About :- /tss/about
def about(request):
    return render(request, 'shop/about.html')
    
# Shop Asset_Management :- /tss/about
def Asset_Management(request):
    return render(request, 'shop/Asset_Management.html')

# Shop ContactUs:- /tss/contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Render the email template for the admin
        email_html_message = render_to_string('shop/email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        email_message = EmailMessage(
            subject,
            email_html_message,
            settings.CONTACT_EMAIL,
            [settings.CONTACT_EMAIL],
            headers={'Reply-To': email}
        )
        email_message.content_subtype = 'html'  # Set the email content type to HTML
        email_message.send()

        # Render the email template for the client
        client_email_html_message = render_to_string('shop/client_email_template.html', {
            'name': name,
            'subject': subject,
            'message': message,
        })

        client_email_message = EmailMessage(
            'Thank you for contacting us',
            client_email_html_message,
            settings.CONTACT_EMAIL,
            [email],
            headers={'Reply-To': settings.CONTACT_EMAIL}
        )
        client_email_message.content_subtype = 'html'  # Set the email content type to HTML
        client_email_message.send()

        return JsonResponse({'success': True})

    return render(request, 'shop/contact-us.html')


# Shop our-commitments:- /tss/contact 
def commitments(request):
    return render(request, 'shop/our-commitments.html')

# Shop our-iConcept4_Pro:- /tss/contact
def iConcept4_Pro(request):
    return render(request, 'shop/iConcept4_Pro.html')

# Shop our-iConcept4_Pro:- /tss/contact
def efass(request):
    return render(request, 'shop/efass.html')

# Shop our-RadraPro:- /tss/contact
def RadraPro(request):
    return render(request, 'shop/RadraPro.html')

# Shop request_demo:- /tss/contact
def request_demo(request):
    return render(request, 'shop/request_demo.html')

# Shop Faqs:- /tss/contact
def faqs(request):
    return render(request, 'shop/faqs.html')

# Shop Items :- /shop
def shop(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items'] # Items in Cart
    
    context = {
        'products': products,
        'cartItems': cartItems,
        'items': items,
    }
    return render(request, 'shop/shop.html', context=context)

# Item Cart :- tss/cart/
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items, # items in the cart
        'order': order, # order object for the customer
        'cartItems': cartItems, # cart item count
        'shipping':False, # shiiping boolean value to ask for address or not
    }
    return render(request, 'shop/cart.html', context=context)

@login_required
# Checkout tss/checkout
def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,   # items in the cart 
        'order': order,   # order object for the customer
        'cartItems': cartItems,  # cart item count
        'shipping':False   # shiiping boolean value to ask for address or not
    }
    return render(request, 'shop/checkout.html', context=context)

# Item Detail
# def itemDetail(request):
#     return render(request, 'shop/item-detail.html')

# To update Items in the cart of the customer
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print('Product: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    orderItem.quantity+= 1 if action == 'add' else -1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)

# Function to process Order
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        # Creating Customer
        customer = request.user.customer
        customer.fname = data['user']['firstName']
        customer.lname = data['user']['lastName']
        customer.email = data['user']['email']

        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        total = float(data['user']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True

        order.save()

        if order.shipping == True:
            ShippingAdress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address']+' '+data['shipping']['address2'],
                city=data['shipping']['country'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zip'],
            )
    else:
        return redirect('login')

    return JsonResponse('Payment Complete', safe=False)
