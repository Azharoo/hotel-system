from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello world from django')

def Home_page(request):
    return HttpResponse("""<h1>Welcome from Django 1.11</h1>
    <h3 style="color:red; text-align: center">Thank you 
    <span style="color:#000">Mr.Shadi</span> !!</h3>""")