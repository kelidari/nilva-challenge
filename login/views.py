from django.shortcuts import  render,redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:list')
        else:
            form = UserCreationForm()
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form': form})