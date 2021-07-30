from django.shortcuts import redirect, render
import razorpay
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        amount=int(request.POST['amount']) * 100
        client=razorpay.Client(auth=('rzp_live_0ed3Q2fiX6S0x2','6rTvlvDoeeMzCSYwCEHReyi2'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        coffee=Coffee(name=name,amount=amount,payment_id=payment['id'])
        coffee.save()
        return render(request,'index.html',{'payment':payment})

    return render(request,'index.html')
@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        print(a)

    return render(request,"success.html")