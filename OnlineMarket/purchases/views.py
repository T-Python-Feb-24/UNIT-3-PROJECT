from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from product.models import Product
from .models import Cart
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def product_cart_view(request: HttpRequest, product_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    try:
        product = Product.objects.get(pk=product_id)

        #check if user already favored this post
        product_cart = Cart.objects.filter(user=request.user, product=product).first()

        if not product_cart:
            cart = Cart(user=request.user, product=product)
            cart.save()
            return redirect("purchases:cart_view")
    
    except Exception as e:
        print(e)
    return redirect("product:product_detail_view", product_id=product_id)



def cart_view(request:HttpRequest):
    user=request.user
    cart_item= user.cart_set.all()
    total_price=sum(item.product.price for item in cart_item)
    return render(request,"purchases/cart.html",{"user":user,"cart_item":cart_item,"total_price":total_price})

def delete_product_view(request:HttpRequest,product_id):
     
     try:
        cart = Cart.objects.get(user=request.user,product=product_id)
        cart.delete()
     except Exception as e:
        print(e)
     return redirect('purchases:cart_view')

def checkout_view(request:HttpRequest):
    if request.method == 'POST':
     
        user=request.user
        cart_item = user.cart_set.all()  # Example, replace with actual retrieval logic
        total_price=sum(item.product.price for item in cart_item)
        subject = 'Purchase Invoice'
        message = 'test msg'
        send_html_email_to_user(subject,message,user.email)
        return render(request, 'purchases/order_success.html')
    else:
        
        user=request.user
        cart_item = user.cart_set.all()  # Example, replace with actual retrieval logic
        total_price=sum(item.product.price for item in cart_item)
        return render(request, 'purchases/checkout.html', {'cart_item': cart_item, 'total_price': total_price})




def send_html_email_to_user(subject,msg,user_email):
    subject = subject
    message = msg
    email_from =settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    email = EmailMessage(subject, message, email_from, recipient_list)
    email.content_subtype = 'html'  # Enable HTML content
    try:
        email.send()
    except Exception as e:
        print(e)