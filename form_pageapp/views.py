from django.shortcuts import render
from form_pageapp.forms import UserForm
from form_pageapp.models import RegistrationUser
# Create your views here.

def registrationuserform(request): 
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            
            form.save()
            user = RegistrationUser.objects.order_by('-id').first() 
            user = {'user':user}
            return render (request,'form_pageapp/success.html',context=user)

        else:
            return render(request,'form_pageapp/register.html',{'form': form})
        
    else:
        form = UserForm()
    return render(request, 'form_pageapp/register.html',{'form':form})




