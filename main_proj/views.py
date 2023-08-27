from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



def homePage(request):
    
    return render(request,"homepage.html")

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login/')

    else:
        return render(request,'login.html')

def signUp(request):

    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup/')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,'Email Taken')
            #     return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1)
                user.save();
                messages.info(request,'user created')
                return redirect('/login/')

        else:
            messages.info(request,'password not matching..')    
            return redirect('/signup/')

        # return redirect('/')
        
    else:
        return render(request,'signup.html')

def about(request):
    
    return render(request,"About.html")

def contactUs(request):
    
    return render(request,"contactus.html")

def pest(request):
    
    return render(request,"pest.html")

def weed(request):
    
    return render(request,"weed.html")

def camera(request):
    
    return render(request,"camera.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


# def sec(request):
#     return HttpResponse("welcome to 2nd url")

# def abdetail_func(request,detailid):
#     return HttpResponse(detailid) 

# def aboutUS(request):
#     # return HttpResponse("<h1>welcome to nayapalli</h1>")
#     return render(request,"aboutus.html")