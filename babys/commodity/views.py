from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import *
from django.http import JsonResponse
from django.db.models import F

def detailView(request, id):
    title = '商品介绍'
    classContent = 'datails'
    commoditys = CommodityInfos.objects.filter(id=id).first()
    items = CommodityInfos.objects.exclude(id=id).order_by('-sold')[:5]
    likesList = request.session.get('likes', [])
    likes = True if id in likesList else False
    return render(request, 'details.html', locals())


def commodityView(request):
    title = '商品列表'
    classContent = 'commoditys'
    # 根据模型Types生成商品分类列表
    firsts = Types.objects.values('firsts').distinct()
    typesList = Types.objects.all()
    # 获取请求参数 t 商品分类， s 商品排序， p 分页显示, n 商品关键字查询。
    #（）内前者为传入参数，后者为默认的传入参数 ，比如t为 寻找名为 t 的GET参数，而且如果参数没有提交，返回一个空的字符串。这样不会报错
    t = request.GET.get('t', '')
    s = request.GET.get('s', 'sold')
    p = request.GET.get('p', 1)
    n = request.GET.get('n', '')

    # 根据请求参数查询商品信息
    commodityInfos = CommodityInfos.objects.all()
    if t:
        # t为查询某个分页的商品信息，以整型格式表示，代表模型Type的主键id， 首先查询Type的字段id=t的数据A，然后从数据A中取出字段seconds的数据B，最后查询模型CommodityInfos等于数据B的数据，从而得到某个分页的商品信息
        #.first()为python的方法，取Query的第一个值
        # filter(id=t) id为Type模型中的字段id， commodityInfos.filter(types=types.seconds) 为CommodityInfos中过滤types字段的数据
        #更多查询条件filter和get的匹配符见书中的79页
        types = Types.objects.filter(id=t).first()
        commodityInfos = commodityInfos.filter(types=types.seconds)
    if s:
        #变量s是设置商品的排序方式，如果请求为空，则默认变量s等于字符串sold，而sold代表CommodityInfos模型中的sold字段，因此请求参数为s的值
        # 为sold、price、created、likes分别对应模型的字段sold、price、created、likes
        commodityInfos = commodityInfos.order_by('-' + s)
    if n:
        # 模型CommodityInfos的字段name进行模糊匹配，英雌查询条件为name__contains=n
        commodityInfos = commodityInfos.filter(name__contains=n)
    # p 分页功能，默认变量p为1，代表当前第一页的信息
    # 每页显示6个数据（6条商品信息）
    paginator = Paginator(commodityInfos, 6)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'commodity.html', locals())



def collectView(request):
    id = request.GET.get('id', '')
    result = {"result": "已收藏"}
    likes = request.session.get('likes', [])
    if id and not int(id) in likes:
        # 对商品的收藏数量执行自增加1
        CommodityInfos.objects.filter(id=id).update(likes=F('likes')+1)
        result['result'] = "收藏成功"
        request.session['likes'] = likes + [int(id)]
    return JsonResponse(result)