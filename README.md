 
**What are Cookies?**
Cookies are small pieces of data stored in the user's browser.
They help the server remember information about the user across multiple requests


**Flow of Cookies**
-->User enters data in form
-->Server stores data in cookie
-->Browser saves cookie
-->Next request lo cookie send chestundi
-->Server reads and uses it





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
