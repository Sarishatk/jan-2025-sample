from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate,login
from UserApp.forms import registrationForm,LoginForm
# Create your views here.

class registerview(View):
    def get(self, request):

        form = registrationForm

        return render(request,"register.html",{'form':form})
    
    def post(self, request):

        form = registrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)   
            user.set_password(form.cleaned_data['password'])
            user.save()

            form = registrationForm()

            return render(request,"register.html",{'form':form})
        

class LOginView(View):

    def get(self, request):

        form = LoginForm()

        return render(request,"login.html",{'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                form = registrationForm()
                return render(request,"register.html",{'form':form})   

            


    

    
