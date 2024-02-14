from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def home_page(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile_view(request):
    profile = request.user
    context = {'profile': profile}
    return render(request, 'profile.html', context)


