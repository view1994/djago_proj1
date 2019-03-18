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
    login = BooleanField( default= False)
    usr_name = StringField()
    email = StringField( primary_key= True )
    password = StringField( min_length = 8 )
    regis_date = DateField( )
    facial_count = IntField( default= 0 )

    meta = {'collection': 'AccountInfo'}

class FacialFeature(Document):
    name = StringField()
    facial_feature = ListField(ListField())

