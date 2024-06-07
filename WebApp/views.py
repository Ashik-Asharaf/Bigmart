from django.shortcuts import render,redirect
from Backend.models import ProductDB,Bigdb
from WebApp.models import ContactDb,RegDb,CartDb
from django.contrib import messages

# Create your views here.

def home_pg(req):
    cat= Bigdb.objects.all()
    return render(req,'home.html', {'cat':cat})
def about_pg(req):
    cat= Bigdb.objects.all()
    return render(req,'about.html', {'cat':cat})
def contact_pg(req):
    cat= Bigdb.objects.all()

    return render(req,'contact.html' , {'cat':cat})
def product_pg(req):
    data=ProductDB.objects.all()
    cat= Bigdb.objects.all()
    return render(req,'our_product.html', {'data':data, 'cat':cat})

def save_contact(req):
    if req.method == "POST":
        na= req.POST.get('name')
        em= req.POST.get('email')
        ph= req.POST.get('phone')
        sb= req.POST.get('subject')
        ms= req.POST.get('message')
        obj = ContactDb(Name = na,Email=em,Phone=ph,Subject=sb,Message=ms)
        obj.save()
        return redirect(contact_pg)


def filter_cate(req,cat):
    fcat = ProductDB.objects.filter(Category= cat)
    return render(req,'filtered.html',{'fcat':fcat})


def single(request,pro_id):
    pro=ProductDB.objects.get(id=pro_id)
    cat= Bigdb.objects.all()

    return render(request,'single_product.html',{'pro':pro,'cat':cat})

def reg_pg(req):
    return render(req,'Registration.html')

def save_reg(req):
    if req.method == "POST":
        rn = req.POST.get('name')
        re = req.POST.get('email')
        ps = req.POST.get('pass')
        obj = RegDb(RaName=rn,RaEmail=re,RPassword=ps)
        if RegDb.objects.filter(RaName=rn).exists():
            messages.warning(req,"User already Exists.....!")
        elif RegDb.objects.filter(RaEmail=re).exists():
            messages.warning(req,"Email id already Exists.....!")
        else:
            obj.save()
        return redirect(reg_pg)


def save_cart(req):
    if req.method == "POST":
        na= req.POST.get('uname')
        pn= req.POST.get('pname')
        qt= req.POST.get('quantity')
        tp= req.POST.get('tprice')
        obj = CartDb(UName = na,PName=pn,Quantity=qt,Total=tp)
        obj.save()
        return redirect(single)



