from django.db import models
from django.contrib.auth.models import User

# Create your models here.

JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类")
]

Cities = [
    (0,"上海"),
    (1,"北京"),
    (2,"杭州")
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False,choices=JobTypes,verbose_name="职位类别")
    job_name = models.CharField(max_length=250,blank=False,verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False,choices=Cities,verbose_name="工作地点")
    job_reponsibility = models.TextField(max_length=1024,blank=False,verbose_name="职位责任")
    job_requirement = models.TextField(max_length=1024,blank=False,verbose_name="职位要求")
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name="发布人")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="创建日期")
    modified_date = models.DateTimeField(auto_now=True,verbose_name="修改时间")
    