from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import LoginForm, RegistrationForm


class LoginUser(auth_views.LoginView):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "accounts/auth.html", context={
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("profile")


class LogoutUser(auth_views.LogoutView):
    next_page = reverse_lazy('start_page')


class UserCreateView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'

    def __init__(self):
        self.object = None

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


@login_required
def user_profile(request):
    return render(request, 'accounts/lk.html', 
                  context={'username': request.user.get_username()})
