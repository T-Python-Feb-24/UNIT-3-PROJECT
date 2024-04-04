from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Order 
# Create your views here.

def order_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("accounts:login_page")

    if request.method == 'POST':
        try:
            new_order = Order(
                user=request.user,
                subject=request.POST["subject"],
                description=request.POST["description"],
                state=request.POST.get("state","Under review"),
                file=request.FILES.get("file")
            )
            new_order.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)

    return render(request, "requests/order_page.html")



def order_update_page(request: HttpRequest, order_id):    
    if not request.user.is_authenticated:
        return redirect("accounts:login_page")
    
    order = Order.objects.get(pk=order_id)

    if request.user != order.user and not request.user.is_staff:
        return redirect("main:no_permission")

    if request.method == "POST":
        try:
            if "subject" in request.POST: 
                order.subject = request.POST["subject"]
            if "description" in request.POST:
                order.description = request.POST["description"]
            if "state" in request.POST:
                order.state = request.POST.get("state", "Under review")

            if "file" in request.FILES:
                order.file = request.FILES["file"]

            order.save()
            return redirect("accounts:dashborad_page")
        except Exception as e:
            print(e)

    return render(request, 'requests/order_update_page.html', {"order": order, "states": Order.states.choices})


def delete_order(request:HttpRequest,order_id):

    # if not request.user.is_staff:
    #     return render(request, "main/no_permission.html")

    try:
        order = Order.objects.get(pk=order_id)
        if request.user == order.user:
            order.delete()
    except Exception as e:
        print(e)

    
    return redirect("accounts:dashborad_page")

    
        