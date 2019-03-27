from django.db import models

from mongoengine import *
from mongoengine import connect
connect('wbsite', host='127.0.0.1', port=27017)
# ORM
# Create your models here.
class AccountInfo(Document):
    '''
        账号信息数据库数据结构
    '''
    login_flag = BooleanField( default= False)
    usr_name = StringField(primary_key= True)
    password = StringField( min_length = 6 )
    regis_date = DateField( )
    facial_count = IntField( default= 0 )

    meta = {'collection': 'AccountInfo'}

class FacialFeature(Document):
    name = StringField()
    facial_feature = ListField(ListField())

