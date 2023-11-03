from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # may be need change
            username = form.clean_username()
            messages.success(request,
                             f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',
                  {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES,
                                  instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request,
                             f'Updated')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'uform': uform,
        'pform': pform
    }
    return render(request, 'users/profile.html',
                  context=context)


class OtherProfileView(DetailView):
    context_object_name = 'object'
    template_name = 'users/other.html'
    model = Profile
    fields = ['username', 'image', 'bio']

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        obj = self.model.objects.get(pk=pk)
        return obj
