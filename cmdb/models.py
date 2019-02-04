from django.db import models

# Create your models here


class cmdb_new (models.Model):    # index是Class的名称与views的相同，也是创建的表名
    mID = models.IntegerField
    mNAME = models.TextField(max_length=64)# 创建Char 类型字段，字段长度为64，根据自己实际需求进行更改。
    mPASSWORD = models.TextField(max_length=64)
