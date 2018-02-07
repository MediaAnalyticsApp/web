from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse
from authapp.forms import UserRegisterForm
from authapp.forms import UserEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def login(request):
    title = 'Вход'
    login_form = UserLoginForm(data=request.POST or None)

    _next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main:index'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': _next
    }

    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
            edit_form = UserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)


def change_password(request):
    title = 'Изменение пароля'

    if request.method == 'POST':
        change_pass_form = PasswordChangeForm(data=request.POST, user=request.user)

        if change_pass_form.is_valid():
            change_pass_form.save()
            update_session_auth_hash(request, change_pass_form.user)
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        change_pass_form = PasswordChangeForm(user=request.user)

    content = {'title': title, 'change_pass_form': change_pass_form}
    return render(request, 'authapp/change_password.html', content)
