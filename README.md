 


**How Cookies Work in Django**
** Setting a Cookie**
def log(request):
    name = request.GET.get('name')
    response = render(request, 'sview.html', {'se': name})
    response.set_cookie('name', name)
    return response

   ** Getting a Cookie**
def tlog(request):
    name = request.COOKIES.get('name', 'Guest')
    return render(request, 'tview.html', {'se': name})
