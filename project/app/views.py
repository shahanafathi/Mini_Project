from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth
from .models import CustomeUser,transaction
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import make_password



def index(request):
    return render(request,'login.html')
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
         # Authenticate superusers (admins)
         
         
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request, admin_user)
            return redirect(admin_profile)  # Redirect to the admin dashboard
        elif user is not None:
            # If not an admin, check regular users
            login(request, user)
            if user.usertype == "user":     #user profile
                return redirect(userhome)
            elif user.usertype == "bank":   #agency profile
                return redirect(bankhome)
            # elif user.usertype=="admin":
            #    return HttpResponse('homepage sucess')
            return render(request, 'login.html', context)
        else:
            context = {
                'message': "Invalid credentials"
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
      
        
    
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        Username=request.POST['UserName']
        if CustomeUser.objects.filter(username=Username).exists():
            return render(request,'user/register.html',{'error':'username already exists'})
        age=request.POST['Age']
        InitialAmount=request.POST['InitialAmount']
        Phonenumber=request.POST['Phonenumber']
        if CustomeUser.objects.filter(Phonenumber=Phonenumber).exists():
            return render(request,'user/register.html',{'error':'Phonenumber already exists'})
        AccountNumber=request.POST['AccountNumber']
        if CustomeUser.objects.filter(AccountNumber=AccountNumber).exists():
            return render(request,'user/register.html',{'error':'AccountNumber already exists'})
        dob=request.POST['DOB']
        Address=request.POST['Address']
        Adharnumber=request.POST['Adharnumber']
        if CustomeUser.objects.filter(AdharNumber=Adharnumber).exists():
            return render(request,'user/register.html',{'error':'Adharnumber already exists'})
        Pancardno=request.POST['Pancardno']
        if CustomeUser.objects.filter(Pancardno=Pancardno).exists():
            return render(request,'user/register.html',{'error':'Pancardno already exists'})
        pincode=request.POST['pincode']
        Email=request.POST['Email']
        if CustomeUser.objects.filter(email=Email).exists():
            return render(request,'user/register.html',{'error':'email already exists'})
        Password=request.POST['Password']
        Confirmpassword=request.POST['Confirmpassword']
        if Password!=Confirmpassword:
            return render(request,'user/register.html',{'error':'password not matching'})
        Image=request.FILES['Image']
        # raw_password = 'bank'
        # hashed_password = make_password(raw_password)
        # print(hashed_password)
        data1=CustomeUser.objects.create_user(first_name=name,age=age,email=Email,Image=Image,AccountNumber=AccountNumber,DOB=dob,Address=Address,Pincode=pincode,Pancardno=Pancardno,AdharNumber=Adharnumber,Phonenumber=Phonenumber,InitialAmount=InitialAmount,username=Username,password=Password,usertype='user')
        data1.save()
        return redirect(Login)
    else:
        return render(request,'user/register.html')


# user.............................



def userhome(request):
    usr=CustomeUser.objects.get(id=request.user.id)
    return render(request,'user/home.html',{'data':usr})



def userprofile(request):
    usr=CustomeUser.objects.get(id=request.user.id)
    return render(request,'user/profile.html',{'data':usr})

def profileedit(request,id):
    data1=CustomeUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        data1.first_name=request.POST['Name']
        data1.age=request.POST['age']
        data1.Phonenumber=request.POST['Phonenumber']
        data1.DOB=request.POST['DOB']
        data1.Address=request.POST['Address']
        data1.email=request.POST['Email']  
        data1.username=request.POST['UserName']
        data1.Pancardno=request.POST['Pancardno']
        data1.AdharNumber=request.POST['AdharNumber']
        if 'Image' in request.FILES:
            data1.Image = request.FILES['Image']
        data1.save()
        return redirect(userprofile)
    else:
        return render(request,'user/profileedit.html',{'datas':data1})
    
def userhome1(request):
    data=CustomeUser.objects.get(usertype='bank')
    data1=CustomeUser.objects.get(id=request.user.id)
    return render(request,'user/home1.html',{'data':data,'data1':data1})

def deposite(request):
    data = CustomeUser.objects.get(id=request.user.id)
    if request.method=='POST':
        amount = request.POST['amount']
        data.InitialAmount+=int(amount)
        data.save()
        a = transaction.objects.create(user_id=data,details='Deposit', amount=amount,balance=data.InitialAmount)
        a.save()
        return redirect(userhome)
    else:
        data1=CustomeUser.objects.get(usertype='bank')
        return render(request,'user/deposit.html',{'data':data,'datas':data1})
    
def withdraw(request):
    datas=CustomeUser.objects.get(usertype='bank')
    data1=CustomeUser.objects.get(id=request.user.id)
    if request.method=='POST':
        amount = int(request.POST.get('amount')) 
        # if amount<=0:
        #     return HttpResponse('invalid')
        if data1.InitialAmount <= amount or data1.InitialAmount-amount<1000:
            context={'message':'insufficient balance'}
            return render(request,'user/withdraw.html',context)
        data1.InitialAmount-=amount
        data1.save()
        a=transaction.objects.create(user_id=data1,details='Withdrawel',amount=amount,balance=data1.InitialAmount)
        a.save()
        return redirect(userhome)
    else:
        return render(request,'user/withdraw.html',{'data':data1,'datas':datas})
    
def viewhistory(request):
    datas = transaction.objects.filter(user_id=request.user.id)
    return render(request,'user/viewhistory.html',{'data':datas})
        
    
       
# Bank.............................................




def bankhome(request):
    data11=CustomeUser.objects.filter(usertype='user').count()
    return render(request,'bank/home.html',{'data3':data11})
    

def  profileview(request):
    data1=CustomeUser.objects.get(id=request.user.id)
    return render(request,'bank/profileview.html',{'data':data1})


def viewuser(request):
        users = CustomeUser.objects.filter(usertype='user')
        return render(request,'bank/viewusers.html',{'users': users})
    
def search(request):
    if request.method=='POST':
        Search=request.POST['search']
        user = CustomeUser.objects.filter(usertype='user',first_name__icontains=Search)
        return render(request,'bank/viewusers.html',{'users': user})
    else:
        return redirect(viewuser)
    
def all(request):
    return redirect(viewuser)
    
def bankuserprofile(request,id):
    users= CustomeUser.objects.get(id=id)
    return render(request,'bank/profileview.html',{'user':users})
    
    
def userhistory(request,id):
    datas = transaction.objects.filter(user_id=id)
    users= CustomeUser.objects.get(id=id)
    return render(request,'bank/profilehistory.html',{'data':datas,'user':users})
   
def logout(request):
    auth.logout(request)
    return redirect(Login)


# Admin.............................................


def admin_home(request):
    if request.method == "POST":
        name = request.POST['name']
        Branch =  request.POST['branch']
        ifsc = request.POST['ifsc']
        Pincode = request.POST['pincode']
        Username = request.POST['UserName']
        if CustomeUser.objects.filter(first_name=name).exists():
            return render(request,'admin/adminregstr.html',{'error':"bank already exist"})
        Password = request.POST['Password']
        if CustomeUser.objects.filter(first_name=name).exists():
            return render(request,'admin/adminregstr.html',{'error':"bank already exist"})
        data= CustomeUser.objects.create_user(first_name=name,Branch=Branch,Ifsc=ifsc,Pincode=Pincode,username=Username,password=Password,usertype="bank")
        data.save()
        return redirect(admin_profile)
    else: 
        return render(request,'admin/adminregstr.html')
    
    
def admin_profile(request):
    datas=CustomeUser.objects.filter(usertype='bank')
    print(datas)
    return render(request,'admin/viewbank.html',{'data':datas})

