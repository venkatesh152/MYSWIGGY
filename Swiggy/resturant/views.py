from django.contrib import messages
from django.shortcuts import render,redirect
from resturant.forms import *
from resturant.models import *

def mainpage(request):
    return render(request,"resturant/main.html")


def reg(request):
    return render(request,"resturant/reg.html",{"data":ResturantForm()})


def save(request):
    rf = ResturantForm(request.POST)
    if rf.is_valid():
        rg = rf.save(commit=False)
        rg.res_otp = 1234
        rg.res_status = "pending"
        rg.save()
        messages.success(request,"your data is stored successfully,we can mail to you once it aproved")
        return redirect('main')
    else:
        return render(request,"resturant/reg.html",{"data":rf})