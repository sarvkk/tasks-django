from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now=datetime.datetime.today()
    return render(request,'index.html',
                  {
                      "newyear":  now.month==1 and now.day==1
                  }
)
    
def ram(request):
    return HttpResponse("helloworld")