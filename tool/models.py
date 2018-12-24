from django.db import models

# Create your models here.
from mongoengine import *
from datetime import datetime

connect('questionnaire')

class Info(Document):
    #SequenceField() #自动产生一个数列、 递增的
    #unique=True给Field构造函数来指定一个字段在集合中是唯一的
    #title = StringField(unique=True)
    title = StringField()
    content = ListField(default=[[]])#列表里存储字符串数据
    number = IntField()
    date = DateTimeField(default=datetime.utcnow)#default默认
    #required是否必须赋值 true false 
    #ordering属性 指定默认排序
    meta = {
        'ordering': ['-date']
    }
    def save(self):
        self.number = datetime.now().microsecond
        return super(Info, self).save()
    
    
    #title = ReferenceField(Title)

    #要使引用字段可以存储到数据库中的其他文档，可以使用 ReferenceField。
    #传入另一个文档类作为构造函数的第一个参数，然后将文档对象分配给该字段

#StudentModel.objects.create(name='klc',age=18)
#StudentModel.objects.filter(name='klc').delete()
#StudentModel.objects.filter(name='klc').update(age=16)
#a = StudentModel.objects.all()
