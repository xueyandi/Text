import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from common import md5_
from .models import *

from homess import settings

# Create your views here.
def log(request):
    return redirect('/login/')

def login(request):
    print('--->', request.method)
    if request.method == 'POST':
        print(request.POST)

        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        login_user = TSysUser.objects.filter(username=username, auth_string=password_).first()
        if login_user:
            # 系统管理员
            role_ = login_user
            role1_ = login_user.role_id
            login_info = {
                '_id': login_user.id,
                'name': role_.username,
                'code': 'admin'
            }

            if not error:
                request.session['login_user'] = login_info
                return redirect('/')
    return render(request, 'login.html', locals())

def logout(request):
    del request.session['login_user']
    return redirect('/login/')


@csrf_exempt
def block_settings(request):
    return render(request, 'settings.html', locals())

def index(request):
    return render(request, 'dashboard.html')

def message(request):
    objs = TAdvertising.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        TAdvertising.objects.get(pk=request.GET.get('a_id')).delete()

    return render(request, 'message/list.html', locals())

def music(request):
    objs = CMusic.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        CMusic.objects.get(pk=request.GET.get('a_id')).delete()

    return render(request, 'music.html', locals())

# def modify_music(request):
#     action = request.GET.get('action', '')
#     obj = CMusic.objects.get(pk=request.GET.get('m_id'))
#     if action == 'no':
#         obj.state = 2  # request params {note}
#         obj.note = request.GET.get('note', '')
#         obj.save()
#
#     if action == "yes":
#         obj.state = 1
#         obj.save()
#
#     return redirect('/music/')

# def music(request):
#     objs = CMusic.objects.filter(state=0).all()
#     return render(request, 'music.html', locals())



def modify_article(request):
    action = request.GET.get('action', '')
    obj = CArticle.objects.get(pk=request.GET.get('a_id'))
    if action == 'no':
        obj.state = 2  # request params {note}
        obj.note = request.GET.get('note', '')
        obj.save()

    if action == "yes":
        obj.state = 1
        obj.save()

    return redirect('/article/')

def article(request):
    objs = CArticle.objects.filter(state=0).all()
    return render(request, 'article.html', locals())


def role(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSysRole.objects.get(pk=request.GET.get('role_id')).delete()

    roles = TSysRole.objects.all()
    return render(request, 'role/list.html', locals())

def list_sys_user(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSysUser.objects.get(pk=request.GET.get('id')).delete()

    # 查询系统时，除去超级管理员的用户
    users = TSysUser.objects.filter(~Q(pk=request.session['login_user']['_id'])).all()
    return render(request, 'sys_user/list.html', locals())

class EditRoleView(View):
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = TSysRole.objects.get(pk=role_id)
        return render(request, 'role/edit.html', locals())

    def post(self, request):
        from .forms import RoleForm
        role_id = request.POST.get('id', '')
        if role_id:
            form = RoleForm(request.POST, instance=TSysRole.objects.get(pk=role_id))
        else:
            form = RoleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/role/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'role/edit.html', locals())

class EditSysUserView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TSysUser.objects.get(pk=id_)

        roles = TSysRole.objects.filter(~Q(code='admin'))
        return render(request, 'sys_user/edit.html', locals())

    def post(self, request):
        from .forms import SysUserForm
        id_ = request.POST.get('id', '')
        if id_:
            form = SysUserForm(request.POST, instance=TSysUser.objects.get(pk=id_))
        else:
            form = SysUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_sysuser/')

        errors = json.loads(form.errors.as_json())

        roles = TSysRole.objects.filter(~Q(code='admin'))

        return render(request, 'sys_user/edit.html', locals())

class EditMessageView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TAdvertising.objects.get(pk=id_)

        return render(request, 'message/edit.html', locals())

    def post(self, request):
        from .forms import MessageForm
        id_ = request.POST.get('id_', '')
        if id_:
            form = MessageForm(request.POST, instance=TAdvertising.objects.get(pk=id_))
        else:
            form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/message/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'message/edit.html', locals())


class AuditMessage(View):
    def get(self, request):
        action = request.GET.get('action', '')
        if action:
            obj = TAdvertising.objects.get(pk=request.GET.get('a_id'))
            if action == 'yes':
                obj.state = 1
            elif action == 'no':
                obj.state = 2
                obj.note=request.GET.get('note', '')
            obj.save()
            obj.full_clean()


        objs = TAdvertising.objects.filter(state=0).all()
        return render(request, 'message/list_audit.html', locals())