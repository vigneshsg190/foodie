from pyexpat.errors import messages
from tokenize import Name
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse
from .models import products, usersignin,cartsaved,finalorder
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.template import loader


# Create your views here.
def newfunc(request):
    return render(request,'index.html')
def homefunc(request):
    return render(request,'index.html')    
def menufunc(request):
    return render(request,'menu.html')  
def aboutfunc(request):
    return render(request,'about.html')
def menufunc(request):
    data=products.objects.filter().all()  
    return render (request,'menu.html',{'data':data}) 
    
   # return render(request,'cart.html')    
def loginfunc(request):
   return render(request,'login.html')  
def signinfunc(request):
    return render(request,'signin.html')  
def registerfunc(request):
    if request.method=='POST':
        n1=request.POST["name"]
        n2=request.POST["password"]
        n3=request.POST["contact_num"]
        n4=request.POST["address"]
        s=usersignin(name=n1,password=n2,contact_num=n3,address=n4)
        s.save() 
        #messages.success(request,'The New User'+request.POST['name']+'Is Saved Successfully....!')
        return render (request,'login.html')
        #return HttpResponse("saved")
    else:
        return render (request,'signin.html')  

def adminurlfunc(request):
    return HttpResponseRedirect('admin/')

def maincartfunc(request,prid):
   if request.method =='POST':
        usrid=request.session['usrid']
        prid = request.POST["prid"]
        qty = request.POST["qty"]
        usr = usersignin.objects.get(usrid=usrid)
        product =products.objects.get(prid=prid)
        c = cartsaved(usrid=usr,prid=product,product_qty=qty)
        c.save()
        return HttpResponseRedirect('/menu')
 
    
def userlogcheckfunc(request):
    if request.POST:
        name = request.POST["name"]
        password = request.POST["password"]
        datac=usersignin.objects.filter(name=name,password=password).count()
        if datac==1:
            data=usersignin.objects.get(name=name,password=password)
            request.session['usrid']=data.usrid
            request.session['name']=data.name
            request.session['password']=data.password
            response=redirect("/userhome")
            return response
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def logoutfunc(request):
    try:
        del request.session['username']
        response = redirect("/index?id=logout")
        return response
    except:
        response = redirect("/index?id=logout")
        return response

#user name printing  from  DB
def userhomefunc(request):
    curntuser=request.session['usrid']
    data=usersignin.objects.filter(usrid=curntuser).all()
    return render(request,"userhome.html",{"data1":data})

def userprofilefunc(request):
    curntusr=request.session['usrid']
    data1=usersignin.objects.filter(usrid=curntusr).all()
    return render(request,"userprofile.html",{"data":data1})
   

def useraboutfunc(request):
   return render(request,'userabout.html')  

def userupdatefunc(request,usrid):
    data=usersignin.objects.get(usrid=usrid)
    return render(request,'userupdate.html',{'data':data})  

#updated user data's re storing in db
def updatercdfunc(request,usrid):
     if request.method =='POST':
        data1 = request.POST['name']
        data2 = request.POST['contact_num']
        data3 = request.POST['address']
        member = usersignin.objects.get(usrid=usrid)
        member.name = data1
        member.contact_num = data2
        member.address = data3
        member.save()
        return HttpResponseRedirect('/userhome')  

def orderfunc(request,prid):
    if request.method =='POST':
        usrid=request.session['usrid']
        prid = request.POST["prid"]
        qty = request.POST["qty"]
        usr = usersignin.objects.get(usrid=usrid)
        product =products.objects.get(prid=prid)
        total=int(product.price)*int(qty)
        c = cartsaved(usrid=usr,prid=product,product_qty=qty,total=total)
        c.save()
        return HttpResponseRedirect('/menu')

def cartfunc(request):
    curntusr=request.session['usrid']
    data1=cartsaved.objects.filter(usrid=curntusr).all()
    return render(request,"cart.html",{"data1":data1})
   

def cartdeletefunc(request,cartid):
    data=cartsaved.objects.get(cartid=cartid)
    data.delete()
    return HttpResponseRedirect('/cart')

#navbar urls
def myordersfunc(request):
    curntusr=request.session['usrid']
    data=finalorder.objects.filter(usrid=curntusr).all()
    return render(request,"myorders.html",{"data":data})


def finalordrfunc(request,cartid):
    if request.method =='POST':  
        usrid=request.session['usrid']
        cartid = request.POST.get("cartid")
        prid1 = request.POST.get("prid_num")
        product_qty = request.POST.get("prd_qty")
        product_total = request.POST.get("prd_total")
        usr = usersignin.objects.get(usrid=usrid)
        prid =products.objects.get(prid=prid1)
        cartid =cartsaved.objects.get(cartid=cartid,total=product_total)
        s = finalorder(cartid=cartid,usrid=usr,prid=prid,product_qty=product_qty,total=product_total)
        s.save()
        cartsaved.objects.filter(usrid=usrid).delete()
        return HttpResponseRedirect('/cart')  
    
  

                     

     


