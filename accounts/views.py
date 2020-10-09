from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from django.views import generic
from django.shortcuts import render, redirect

from .forms import EmailUpdateForm, ProfileUpdateForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('movies-home')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def EmailChangeView(request):
    if request.method == 'POST':
        e_form = EmailUpdateForm(request.POST, instance=request.user)

        if e_form.is_valid():
            e_form.save()
            messages.success(request, f'Twój email został zaktualizowany!')
            return redirect('profile')
    else:
        e_form = EmailUpdateForm(instance=request.user)

    context = {
        'e_form': e_form,
    }
    return render(request, 'accounts/email_change.html', context)

@login_required
def AvatarChangeView(request):
    if request.method == 'POST':    
        a_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if a_form.is_valid():            
            a_form.save()
            messages.success(request, f'Twoje konto zostało zaktualizowane!')
            return redirect('profile')

    else:
        a_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'a_form': a_form
    }

    return render(request, 'accounts/avatar_change.html', context)
