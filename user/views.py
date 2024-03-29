from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from . forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.db import IntegrityError
from django.contrib import messages
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        try:  
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()  
            login(request, newUser)
            messages.success(request,"Başarıyla kayıt oldunuz")
            return redirect("index")
        
        except IntegrityError:  # Kullanıcı adı benzersiz değilse
            form.add_error("username","Bu kullanıcı adı zaten kullanılıyor")
    else: 
        form = RegisterForm()
    context = {
        "form": form,
        'message': 'Kayıt başarılı!'
    }
    return render(request, "register.html", context)







def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form

    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya Parola Hatalı")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
    