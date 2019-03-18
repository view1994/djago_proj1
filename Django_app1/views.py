from django.shortcuts import render

# Create your views here.
account_login = False

def FR_home_page(request):
    return  render(request, '../templates/home.html')

def FR_login_page(request):
    return  render(request, '../templates/login.html')

def FP_register_page(request):
    return render(request, '../templates/register.html')

def FP_home(request):
    if account_login:
        return FR_home_page(request)
    else:
        return FR_login_page(request)

def hello_view(request):
    return render(request, '../templates/hello_view.html')
