from django import contrib
from django.http import request
from django.shortcuts import render, redirect
from backend.models import category, proddetails, contactdb
from frontend.models import deatilescustomer
from django.contrib import messages


def homehtmlpage(request):
    return render(request,"home.html")
def aboutuspage(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")
def homehtmlpage(requst):
    data = category.objects.all()
    return render(requst,"home.html",{'data':data})
def categories(req):
    return render("categorydisplay.html")
def discat(request, itemcatg,):
    print("===itemcatg===",itemcatg)
    catg = itemcatg.upper()
    products=proddetails.objects.filter(Category=itemcatg)
    context={
          'products':products,
            'catg':catg
    }
    return render(request,"categorydisplay.html",context)
# def singlepro(req):
#     return render(req,"singleproduct.html")
def singlepro(request,dataid):
    data = proddetails.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'dat':data})
def registration(request):
    return render(request,"registration.html")
def savecustomer(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        pas = request.POST.get('password')
        Em  = request.POST.get('email')
        Cp  = request.POST.get("confirmpassword")
        if pas==Cp:
            obj = deatilescustomer(Username=Us,Password=pas,confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request,"registered successfully")
        return redirect(registration)
def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if deatilescustomer.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request,"login successfully")
            return redirect(homehtmlpage)
        else:
            messages.error(request,"invalid user")
            return render(request,'registration.html')
def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(homehtmlpage)
def cntct(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        Em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('messege')
    obj = contactdb(Name=na, Email=Em, Subject=sub, messege=msg,)
    obj.save()
    return redirect(contact)






