from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from Backend.models import Bigdb,ProductDB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDb



# Create your views here.
def index_pg(req):
    return render(req,'index.html')

def category_pg(req):
    return render(req,'add_category.html')
def display_cate(request):
    data=Bigdb.objects.all()
    return render(request,"Display_category.html", {'data':data})
def save_category(req):
    if req.method=="POST":
        a=req.POST.get('cname')
        b=req.POST.get('description')
        c=req.FILES['image']

        obj = Bigdb(Cname=a,Description=b,Image=c)
        obj.save()
        return redirect(category_pg)

def edit_cate(req,cate_id):
    data=Bigdb.objects.get(id=cate_id)
    return render(req,"edit_category.html",{'data':data})

def update_category(req,cate_id):
    if req.method=="POST":
        a = req.POST.get('cname')
        b = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Bigdb.objects.get(id=cate_id).Image
        Bigdb.objects.filter(id=cate_id).update(Cname=a, Description=b, Image=file)
        return redirect(display_cate)

def delete_cate(req,cate_id):
    data= Bigdb.objects.filter(id=cate_id)
    data.delete()
    return redirect(display_cate)

def login(request):
    return render(request,'adminlogin.html')
def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('user')
        ps = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x= authenticate(username=un,password=ps)
            if x is not None:
                login(request)
                return redirect(index_pg)
            else:
                return redirect(login)
        else:
            return redirect(login)

def product_pg(req):
    cat= Bigdb.objects.all()
    return render(req,"add_product.html", {'cat':cat})
def display_product (request):
    data=ProductDB.objects.all()
    return render(request,"display_product.html", {'data':data})
def save_product(req):
    if req.method=="POST":
        a=req.POST.get('Category')
        b=req.POST.get('pname')
        c=req.POST.get('price')
        d=req.POST.get('description')
        e=req.FILES['image']

        obj = ProductDB(Category=a,ProductName = b,Price=c,Description=d,ProductImage=e)
        obj.save()
        return redirect(product_pg)

def edit_product(req,pro_id):
    data=ProductDB.objects.get(id=pro_id)
    pro=Bigdb.objects.all()
    return render(req,"edit_pro.html",{'data':data , 'pro':pro})

def update_product(req,pro_id):
    if req.method=="POST":
            a = req.POST.get('Category')
            b = req.POST.get('pname')
            c = req.POST.get('price')
            d = req.POST.get('description')
            try:
                img = req.FILES['image']
                fs = FileSystemStorage()
                file = fs.save(img.name, img)
            except MultiValueDictKeyError:
                file = ProductDB.objects.get(id=pro_id).ProductImage
            ProductDB.objects.filter(id=pro_id).update(Category=a,ProductName = b,Price=c,Description=d,ProductImage=file)
            return redirect(display_product)

def delete_product(req,pro_id):
    data= ProductDB.objects.filter(id=pro_id)
    data.delete()
    return redirect(display_product)

def contact_data(req):
    data = ContactDb.objects.all()
    return render(req,"Contact_Details.html", {'data':data})


def delete_cont(req,cont_id):
    data= ContactDb.objects.filter(id=cont_id)
    data.delete()
    return redirect(contact_data)



