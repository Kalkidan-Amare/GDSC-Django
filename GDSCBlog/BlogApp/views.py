from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_fun(request):

    return render(request,'index.html')
