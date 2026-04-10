from django.shortcuts import render
from testapp. forms import loginform
import datetime

def login_view(request):
    sum=loginform()
    return render(request,'fview.html',{'add':sum})


def log(request):
    name = request.GET['name']
    response=render(request,'sview.html',{'se':name})
    response.set_cookie('se',name)
    return response
# def log(request):
#     name = request.GET.get('name')
#     response = render(request, 'sview.html', {'se': name})
#     response.set_cookie('name', name, max_age=3600)   # 🔥 add max_age also
#     return response



def tlog(request):
    name=request.COOKIES.get('name','Guest')
    
    date=datetime.datetime.now()
    return render(request,'tview.html',{'se':name ,'dat':date})