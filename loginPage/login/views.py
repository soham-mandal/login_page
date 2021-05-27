from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from login.forms import UserAdminCreationForm

@login_required()
def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'login/register.html', {'form': form})

def profile(request):
    context={}
    return render(request, 'login/profile.html', context)