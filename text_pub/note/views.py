from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.http import  HttpResponse
from . import models
from user.models import User
import time
# Create your views here.
#装饰器 验证登录
def check_login(fn):

    def wrap(request,*args,**kwargs):
        if not hasattr(request, 'session'):  # 没有登录过
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request,*args,**kwargs)
    return wrap

@check_login
def list_view(request):
#    此时一定一登录
    user_id = request.session['user']['id']
    #根据一登录的用户id 找到已登录的用户
    auser = User.objects.get(id = user_id)
    notes = auser.note_set.all()
    return render(request,'note/showall.html',locals())
@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request,"note/add_note.html")
    elif request.method == "POST":
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        try:
            anote = models.Note.objects.create(user=auser,title=title,content=content)
            return HttpResponseRedirect('/note/')
        except:
            return HttpResponse('保存失败')
@check_login
def mod_view(request,id):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    try:
        anote = models.Note.objects.get(id=id,user_id=auser.id)
    except:
        return HttpResponse('无效操作')
    if request.method == "GET":
        title = anote.title
        content = anote.content
        return render(request,'note/mod_note.html',locals())
    if request.method == "POST":
        anote.title = request.POST.get('title','')
        anote.content = request.POST.get('content','')
        anote.mod_time = time.ctime()
        anote.save()
        try:
            return HttpResponseRedirect('/note/')
        except Exception as E:
            print(E)
            return HttpResponse('保存失败')

@check_login
def del_view(request,id):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(id=id,user_id=auser.id)
    anote.delete()
    return HttpResponseRedirect('/note/')