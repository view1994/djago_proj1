from django.shortcuts import render
from Django_app1.models import AccountInfo
# Create your views here.
account_login = False

def FR_home_page(request):
    return  render(request, '../templates/home.html')

def FR_login_page(request):
    return  render(request, '../templates/login.html')

def FR_login_confirm(request):
    request.encoding = 'utf-8'
    print ('==login_confirm : request.GET:')
    print(request.GET)
    return render(request, '../templates/home.html')

nameList = []   #all usr name
def FR_register_page(request):
    for i in AccountInfo.objects[:] :
        if i['usr_name'] not in nameList:
            nameList.append(i['usr_name'])
    context = {
        'nameList':nameList
    }
    print(nameList)
    return render(request, '../templates/register.html',context)

def FR_regist_confirm(request):
    #get account info on page，and save in DB
    request.encoding = 'utf-8'
    if ('username'in request.GET) & ('password'in request.GET):
        import datetime
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        usr_name = request.GET['username']
        if usr_name in nameList:
            print('usr name has been used!')
            return FR_register_page(request)
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
    return FR_register_page(request)


def FR_home(request):
    if account_login:
        return FR_home_page(request)
    else:
        return FR_login_page(request)

def hello_view(request):
    return render(request, '../templates/hello_view.html')

#============================================== <<<< DATA GENS >>>> ====================================================

# 不同区域发帖量前三名
def topx(date1,date2,area,limit):

    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$gte':date1,'$lte':date2}},{'area':{'$all':area}}]}},
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
        {'$limit':limit},
        {'$sort':{'counts':-1}}
    ]

    for i in RoomInfo._get_collection().aggregate(pipeline):
        data = {
            'name': i['_id'][0],
            'data': [i['counts']],
            'type': 'column'
        }
        yield data

series_CY = [i for i in topx('2015.12.25','2015.12.27',['朝阳'],3)]
series_TZ = [i for i in topx('2015.12.25','2015.12.27',['通州'],3)]
series_HD = [i for i in topx('2015.12.25','2015.12.27',['海淀'],3)]
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 数据中发帖总量柱状图
def total_post():
    pipeline = [
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    ]

    for i in RoomInfo._get_collection().aggregate(pipeline):
        print(i)
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data

series_post = [i for i in total_post()]


#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def one_day_deal_cate():
    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$gte':'2015.12.25','$lte':'2016.01.11'}},{'time':1}]}},
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
        {'$sort':{'counts':1}}
    ]

    for i in RoomInfo._get_collection().aggregate(pipeline):
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data

def one_day_deal_area():
    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$gte':'2015.12.25','$lte':'2016.01.11'}},{'time':1}]}},
        {'$group':{'_id':{'$slice':['$area',1]},'counts':{'$sum':1}}},
        {'$sort':{'counts':1}}
    ]

    for i in RoomInfo._get_collection().aggregate(pipeline):
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data

pie1_data = [i for i in one_day_deal_cate()]
pie2_data = [i for i in one_day_deal_area()]


#============================================== <<<< PAGE VIEWS >>>> ===================================================
from django.shortcuts import render
from Django_app1.models import RoomInfo
from django.core.paginator import Paginator

def index(request):
    limit = 15
    arti_info = RoomInfo.objects
    paginatior = Paginator(arti_info,limit)
    page = request.GET.get('page',1)
    print(request)
    print(request.GET)
    loaded = paginatior.page(page)

    context = {
        'ItemInfo':loaded,
        'counts':arti_info.count(),
        'last_time':arti_info.order_by('-pub_date').limit(1),

    }

    return render(request,'index_data.html',context)

def chart(request):
    context = {
        'chart_CY':series_CY,
        'chart_TZ':series_TZ,
        'chart_HD':series_HD,
        'series_post':series_post,
        'pie1_data':pie1_data,
        'pie2_data':pie2_data
    }
    return render(request,'chart2.html',context)



