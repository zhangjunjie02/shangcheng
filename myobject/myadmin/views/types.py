#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Types

#用户信息管理
def index(request):
    # '''浏览信息'''
    # list=Types.objects.all()
    list = Types.objects.extra(select={'_has':'concat(path,id)'}).order_by('_has')
    #遍历查询结果，添加一个类别缩进属性
    for ob in list:
        ob.pname = '....'*(ob.path.count(',')-1)

    context={'typeslist':list}
    return render(request,'myadmin/types/index.html',context)



def add(request,tid):
    '''加载添加页面'''

    if tid == '0':
        context={'pid':0,'path':'0,','name':'根类别'}
    else:
        ob=Types.objects.get(id=tid)

        context = {'pid': ob.id, 'path': ob.path+str(ob.id)+',', 'name': ob.name}

    return render(request,'myadmin/types/add.html',context)


def insert(request):
    '''执行添加信息'''
    try:
        ob=Types()
        ob.name=request.POST['name']
        ob.pid=request.POST['pid']


        ob.path = request.POST['path']

        ob.save()
        context={"info":"添加成功"}

    except Exception as err:

        print(err)
        context={"info":"添加失败"}
    return render(request,'myadmin/info.html',context)


def delete(request,tid):
    '''删除信息'''
    try:

        ob = Types.objects.get(id=tid)

        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,'myadmin/info.html',context)

def edit(request,tid):
    '''加载编辑信息页面'''
    try:
        ob = Types.objects.get(id=tid)
        context = {"types": ob}
        return render(request, 'myadmin/types/edit.html', context)
    except Exception as err:
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)

def update(request,tid):
    '''执行编辑信息'''
    try:
        ob=Types.objects.get(id=tid)

        ob.name=request.POST['name']


        ob.save()
        context={"info":"修改成功"}

    except Exception as err:

        print(err)
        context={"info":"修改失败"}
    return render(request,'myadmin/info.html',context)


