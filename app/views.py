from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Ashu','age':2}
    return render(request,'h1.html',d)

def jinja_operation(request):
    d={'a':9,'b':8,'c':80}
    return render(request,'h4.html',d)
    


    