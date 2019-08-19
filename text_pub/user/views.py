from django.shortcuts import render
from django.http import  HttpResponse
from django.http import  HttpResponseRedirect
#加密算法
import hashlib
SAlT = '#YAN' #加盐
# Create your views here.
from .models import *


def reg_view(request):
    # 注册处理视图
    if request.method == 'GET':
        return render(request,'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        try:
            name = User.objects.get(username=username)
            return render(request,"user/register.html",locals())
        except:
            pass
        # 加密
        hash = hashlib.md5((username + SAlT).encode())
        hash.update(password.encode())
        password = hash.hexdigest()
        # 创建cookies
        html = '注册成功'
        html += '<a href="/user/login">前往登录</a>'
        response = HttpResponse(html)
        response.set_cookie('username',username)
        try:
            User.objects.create(username=username,password=password)
        except Exception as e:
            print(e)
            return HttpResponse('注册失败')

        return response

def login_view(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username',"")
        return render(request,"user/login.html",locals())
    elif request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        try:
            hash = hashlib.md5((username + SAlT).encode())
            hash.update(password.encode())
            password = hash.hexdigest()

            auser = User.objects.get(username=username,password=password)


            request.session['user'] = {
                'username':username,
                'id':auser.id
            }
            resp = HttpResponseRedirect('/')
            if 'remember' in request.POST:
                resp.set_cookie('username',username)

            return resp

        except Exception as E:
            print(E)
            password_error = '用户名或密码不正确'
            return render(request,'user/login.html',locals())


def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect('/')