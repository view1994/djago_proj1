from django.shortcuts import render
from Django_app1.models import AccountInfo
# Create your views here.
account_login = False

def FR_home_page(request):
    return  render(request, '../templates/home.html')

def FR_login_page(request):
    return  render(request, '../templates/login.html')

def FP_register_page(request):
    return render(request, '../templates/register.html')

def FP_regist_confirm(request):
    #get account info on page
    request.encoding = 'utf-8'
    print(request.GET)
    if ('username'in request.GET) & ('password'in request.GET):
        import datetime
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_account = AccountInfo(
            login_flag = False,
            usr_name = request.GET['username'],
            password = request.GET['password'],
            regis_date = time,
            facial_count = 0
        )
        new_account.save()

        new_account = {
            'login_flag':False,
            'usr_name':request.GET['username'],
            'password':request.GET['password'],
            'regis_date':time,
            'facial_count':0
        }
        #print(new_account)
        print('\n==account info:\n')
        print(item for item in AccountInfo.objects)
    return render(request, '../templates/login.html')

def FP_home(request):
    if account_login:
        return FR_home_page(request)
    else:
        return FR_login_page(request)

def hello_view(request):
    return render(request, '../templates/hello_view.html')
