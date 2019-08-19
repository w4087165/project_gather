from django.shortcuts import render
from django.http import  HttpResponse
from django.http import  HttpResponseRedirect
# Create your views here.

def index_view(request):
    return render(request,'index/index.html',locals())
