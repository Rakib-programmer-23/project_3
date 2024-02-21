from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author': 'Rahim', 'age':5, 'lst' : [1,2,3], 'courses': [
        {
            'id' : 1,
            'Name': 'Python',
            'Fee' : 1000
        },
        {
            'id' : 2,
            'Name': 'Django',
            'Fee' : 2000
        }
    ]}
    return render(request,"home.html",d)