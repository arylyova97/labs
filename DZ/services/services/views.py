import base64
import json

import time
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse
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
        top_serv = {}
        for service in data:
            top_serv[service] = Order.objects.filter(service=service).count()
        # print(top_serv)
        sort_list = sorted(top_serv.items(), key=lambda item: item[1], reverse=True)
        sort_list = map(lambda x: x[0], sort_list[:5])
        print(sort_list)
        count = {'all': data.count(), 'top': Service.objects.filter(top=True).count()}
        return render(request, 'services/index.html',
                      {'services': sort_list, 'username': auth.get_user(request).username, 'count': count})


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


def create_res(msg, status):
    return HttpResponse(msg, content_type='application/json', status=status)


def get_services(req):
    try:
        if req.method != 'GET':
            return create_res('Only Get', 400)

        limit = int(req.GET['limit'])
        offset = int(req.GET['offset'])

        if not limit and limit != 0 or not offset and offset != 0 or not auth.get_user(req).is_authenticated:
            return create_res('', 400)

        query_set = Service.objects.get_services(limit, offset)
        result = list()
        for service in query_set:
            p = {
                'id': service.id,
                'title': service.title,
                'category': service.category,
                'company': service.company,
                'price': ','.join(str(service.price).split('.')),
                'short_info': service.short_info,
                'top': service.top,
                'img': service.image.url
            }
            result.append(p)
        return create_res(json.dumps(result), 200)
    except Exception as e:
        return create_res(e, 400)


def add_service(req):
    try:
        if req.method != 'POST':
            return create_res('Only Get', 400)

        body = json.loads(req.body.decode('utf-8'))

        if not auth.get_user(req).is_authenticated:
            return create_res('', 400)

        format, imgstr = body['img'].split(';base64,')
        ext = format.split('/')[-1]
        img = ContentFile(base64.b64decode(imgstr), name=str(round(time.time() * 1000)) + '.' + ext)

        service = Service.objects.create(title=body['title'], category=body['category'],
                          company=body['company'], price=float(body['price']),
                          short_info=body['short_info'], image=img)
        service.save()

        return create_res('{}', 200)
    except Exception as e:
        return create_res(e, 400)
