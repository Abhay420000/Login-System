from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class Welcome(View):
    def get(self, request):
        return render(request, 'welcome/index.html')
    
    def post(aelf, request):
        print(request.POST)
        
        if 'logout' in request.POST.keys():
            logout(request)
            return redirect('log_in')
        
        raise Http404("Not Found!")

class Login(View):
    def get(self, request):
        return render(request, 'login/login.html')
    
    def post(self, request):
        
        user = authenticate(username=request.POST["uname"], password=request.POST["pass"])
        
        if user is not None:
            login(request, user)
            return redirect("home_page")
        else:
            return redirect("sign_up")

class SignUp(View):
    def get(self, request):
        return render(request, 'login/signup.html')
    
    def post(self, request):
        print(request.POST)

        try:
            user_name = request.POST["uname"]
            email = request.POST["mail"]
            pwd = request.POST["pwd"]
            
            if (user_name == "") or (email == "") or (pwd == ""):
                return redirect('sign_up')
        except KeyError:
            return HttpResponse("Error!")
        
        user = User.objects.create_user(user_name, email, pwd)
        user.save()
        return redirect('log_in')