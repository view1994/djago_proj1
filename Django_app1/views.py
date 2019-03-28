from django.shortcuts import render
from Django_app1.models import AccountInfo
# Create your views here.
account_login = False

def FR_home_page(request):
    return  render(request, '../templates/home.html')

def FR_login_page(request):
    return  render(request, '../templates/login.html')

nameList = []   #all usr name
def FP_register_page(request):
    for i in AccountInfo.objects[:]:
        nameList.append(i['usr_name'])
    context = {
        'nameList':nameList
    }
    print(nameList)
    return render(request, '../templates/register.html',context)

def FP_regist_confirm(request):
    #get account info on page，and save in DB
    request.encoding = 'utf-8'
    #print(request.GET)
    if ('username'in request.GET) & ('password'in request.GET):
        import datetime
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        usr_name = request.GET['username']
        if usr_name in nameList:
            print('usr name has been used!')
            return FP_register_page(request)
        else:
            new_account = AccountInfo(
                login_flag = False,
                usr_name = usr_name,
                password = request.GET['password'],
                regis_date = time,
                facial_count = 0
            )
            new_account.save()
            print('regist success!')
            return render(request, '../templates/login.html')
    else:
        print('regist failed!')
    return FP_register_page(request)


def FP_home(request):
    if account_login:
        return FR_home_page(request)
    else:
        return FR_login_page(request)

def hello_view(request):
    return render(request, '../templates/hello_view.html')
