from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from services.forms import Login, RegistrationForm
from services.models import Service, Order


def services_list(request):
    return render(request, 'services/services_list.html', {})


class MainPageView(View):
    def get(self, request):
        data = Service.objects.all()
        return render(request, 'services/index.html', {'top_services': data, 'username': auth.get_user(request).username})


class ServicePageView(View):
    def get(self, request, id):
        data = Service.objects.get(pk=id)
        orders = Order.objects.filter(service=id)

        return render(request, 'services/service.html',
                      {'username': auth.get_user(request).username, 'service': data, 'orders': orders})


class ServiceList(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services'


def login(request):
    args = {}
    args['form'] = Login()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'services/login.html', args)
    else:
        return render(request, 'services/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


class UserCreateForm(object):
    pass


class SignUp(FormView):
    template_name = 'services/signin.html'
    form_class = UserCreateForm
    success_url = '/'


def signUp(request):
    # form = None;
    errors = []
    success = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']

            users = User.objects.all()
            usernames = []
            for x in users:
                usernames.append(x.username)

            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                errors.append('Пароли должны совпадать')
            elif usernames.count(username) != 0:
                errors.append('Такой логин уже занят')
            else:
                print("User")
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    # email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    # first_name=form.cleaned_data['first_name'],
                    # last_name=form.cleaned_data['last_name']
                )
                user.save()
                success += 'You was successfully registered.'
                return HttpResponseRedirect('/login/')

    else:
        form = RegistrationForm()
    # form = RegistrationForm(request.POST)
    return render(request, 'services/signin.html', {'form': form, 'errors': errors, 'success': success})
