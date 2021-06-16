from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import *
from django.http import JsonResponse
from django.db.models import F

# 路由detail设置了路由变量id，所以相应的视图函数必须设置相应的函数参数。,在html文件中也要写入id参数

def detailView(request, id):
    title = '商品介绍'
    classContent = 'datails'
    # 商品展示
    commoditys = CommodityInfos.objects.filter(id=id).first()
    # 热销推荐 items查询CommodityInfos前五名销量最高的商品信息，在查询过程中可以使用exclude将当前商品id=id信息排除
    items = CommodityInfos.objects.exclude(id=id).order_by('-sold')[:5]
    #likesList变量是当前用户与django的会话连接，session会话，
    likesList = request.session.get('likes', [])
    # 收藏按钮 likes判断变量likesList是否含有当前商品的主键id，如果当前id已存在变量likesList中，那么说明用户已经收藏了当前商品
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


# 通过读写用户的会话session数据来记录商品的收藏情况，具体的业务逻辑说明如下
def collectView(request):
    # 首先从请求对象request获取请求参数id，并赋值给变量id，它代表当前商品的主键id
    id = request.GET.get('id', '')
    # 然后设置响应内容result，并以字典格式标识
    result = {"result": "已收藏"}
    # 最后从请求对象request获取会话session数据likes，如果存在数据likes，则赋值给变量likes，否则变量likes设置空列表
    likes = request.session.get('likes', [])
    # 如果变量id不为空，并且变量id不在变量likes里面（likes是列表格式）
    # 那么说明当前商品尚未被当前用户加入收藏，程序将执行商品收藏
    if id and not int(id) in likes:
        # 对商品的收藏数量执行自增加1
        # 将变量id作为CommoInfos的查询条件，再有查询对象使用update（）和F（）方法实现
        # 字段likes的自增加1操作；
        CommodityInfos.objects.filter(id=id).update(likes=F('likes')+1)
        # 然后将响应内容result改为收藏过程
        result['result'] = "收藏成功"
        # 最后将当前商品主键id写入会话session数据likes，标记当前商品已经被当前用户收藏了
        request.session['likes'] = likes + [int(id)]
    #     视图函数返回值使用JsonResonse将变量result作为响应内容，JsonResponse能将Python的字典转换为JSON数据。
    # 此外也可以用HttpResponse来实现，不过需要自行将字典转换为JSON数据
    # 比如 HttpResponse(json.dumps(result),content_type='application/json'),首先使用JSON模块转换字典result，然后响应类型content_type要设为application/json

    return JsonResponse(result)