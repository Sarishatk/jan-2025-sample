from django.shortcuts import render
from django.views import View
from UserApp.forms import registrationForm
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

    def get