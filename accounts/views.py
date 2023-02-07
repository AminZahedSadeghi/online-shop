from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserLoginForm, CustomUserCreationForm


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('pages:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'شما با موفقیت وارد اکانت خود شدید :)', 'success')
                if self.next:
                    return redirect(self.next)
                return redirect('pages:home')
            else:
                messages.error(request, 'همچین اکانتی با این مشصخات یافت نشد :/', 'danger')
                return redirect('accounts:login')
        else:
            return render(request, self.template_name, {'form': form})


class UserSignUpView(View):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'شما با موفقیت اکانت خود را ساختید :)', 'success')
            return redirect('accounts:login')
        else:
            return render(request, self.template_name, {'form': form})

