from django.shortcuts import render, redirect
from .models import *
from commodity.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .form import *
from .pays_new import get_pay
import time



# def loginView(request):
#     title = '用户登录'
#     classContent = 'logins'
#     if request.method == 'POST':
#           #获取请求参数，username和password
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         # 查询username的数据是否存在内置模型User
#         if User.objects.filter(username=username):
#             # 验证账号密码与模型User的账号密码是否一致
#             user = authenticate(username=username, password=password)
#             # 通过验证则使用内置函数login执行用户登录
#             # 登录成功后跳转到个人中心页
#             if user:
#                 login(request, user)
#                 # redirect重定向，reverse根据路由命名解析生成相应的路由地址
#                 return redirect(reverse('shopper:shopper'))
#         # username的数据不存在内置模型User
#         else:
#             # 执行用户注册
#             state = '注册成功'
#             # is_staff和is_active设置为普通账户和激活
#             d = dict(username=username, password=password, is_staff=1, is_active=1)
#             user = User.objects.create_user(**d)
#             user.save()
#     # 视图函数loginVIew将模板文件login.html作为响应内容，只要在浏览器输入路由login的路由地址（即向路由login发送GET请求）或者执行用户注册操作（infos）
#     return render(request, 'login.html', locals())

# def loginView(request):
#     title = '用户登录'
#     classContent = 'logins'
#     if request.method == 'POST':
#         infos = LoginForm(data=request.POST)
#         if infos.is_valid():
#             data = infos.cleaned_data
#             username = data['username']
#             password = data['password']
#             if User.objects.filter(username=username):
#                 user = authenticate(username=username, password=password)
#                 if user:
#                     login(request, user)
#                     return redirect(reverse('shopper:shopper'))
#             else:
#                 state = '注册成功'
#                 d = dict(username=username, password=password, is_staff=1, is_active=1)
#                 user = User.objects.create_user(**d)
#                 user.save()
#         else:
#             # 获取错误信息，并以JSON格式输出
#             error_msg = infos.errors.as_json()
#             print(error_msg)
#     else:
#         infos = LoginForm()
#     return render(request, 'login.html', locals())




def loginView(request):
    title = '用户登录'
    classContent = 'logins'
    if request.method == 'POST':
        infos = LoginModelForm(data=request.POST)
        data = infos.data
        username = data['username']
        password = data['password']
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('shopper:shopper'))
        else:
            state = '注册成功'
            d = dict(username=username, password=password, is_staff=1, is_active=1)
            user = User.objects.create_user(**d)
            user.save()
    else:
        infos = LoginModelForm()
    return render(request, 'login.html', locals())


@login_required(login_url='/shopper/login.html')
def shopperView(request):
    title = '个人中心'
    classContent = 'informations'
    # p 代表请求参数和 页数
    p = request.GET.get('p', 1)
    # 处理已支付的订单 t代表用户购买的支付时间
    t = request.GET.get('t', '')
    # paytime来自会话session 也代表用户购买商品的支付时间
    payTime = request.session.get('payTime', '')
    #  通过对比t和paytime。如果两者不为空且相等，则说明该订单已支付成功
    if t and payTime and t == payTime:
        # payinfo获取session订单内容
        payInfo = request.session.get('payInfo', '')
        # 将payinfo写入模型orderinfos，完成用户订单的购买记录；最后在session中删除该订单的支付时间paytime和payinfo
        OrderInfos.objects.create(**payInfo)
        del request.session['payTime']
        del request.session['payInfo']
    # 根据当前用户查询用户订单信息
    orderInfos = OrderInfos.objects.filter(user_id=request.user.id).order_by('-created')
    # 分页功能
    paginator = Paginator(orderInfos, 7)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'shopper.html', locals())

def logoutView(request):
    # 使用内置函数logout退出用户登录状态
    logout(request)
    # 网页自动跳转到首页
    return redirect(reverse('index:index'))


@login_required(login_url='/shopper/login.html')
def shopcartView(request):
    title = '我的购物车'
    classContent = 'shopcarts'
    # 获取请求参数 id 和 quantity购买数量
    id = request.GET.get('id', '')
    quantity = request.GET.get('quantity', 1)
    # 获取当前用户的主键id
    userID = request.user.id
    # 判断id是否为空，
    # 不为空，说明当前请求参数有id和quantity，证明了该请求是用户通过单机商品详细页的：加入购物车触发的
    # 因此要将三个变量新增或更新到CartInfos模型，最后重新访问路由shopcart，再次执行shopcartView函数
    if id:
        CartInfos.objects.update_or_create(commodityInfos_id=id, user_id=userID, quantity=quantity)
        return redirect('shopper:shopcart')
    # getUSerid查找当前用户的购物车信息，然后对getUserid进行遍历赋值给CommodityDict
    getUserId = CartInfos.objects.filter(user_id=userID)
    commodityDcit = {x.commodityInfos_id: x.quantity for x in getUserId}
    # commoInfos： 从CommodityINfos模型中以CommodityDict的键（也就是所有商品的主键id）获取商品的主图、名称和单价
    commodityInfos = CommodityInfos.objects.filter(id__in=commodityDcit.keys())
    return render(request, 'shopcart.html', locals())

def deleteAPI(request):
    result = {'state': 'success'}
    userId = request.GET.get('userId', '')
    commodityId = request.GET.get('commodityId', '')
    if userId:
        CartInfos.objects.filter(user_id=userId).delete()
    elif commodityId:
        CartInfos.objects.filter(commodityInfos_id=commodityId).delete()
    else:
        result = {'state': 'fail'}
    return JsonResponse(result)


def paysView(request):
    total = request.GET.get('total', 0)
    total = float(str(total).replace('￥', ''))
    if total:
        out_trade_no = str(int(time.time()))
        payInfo = dict(price=total, user_id=request.user.id, state='已支付')
        request.session['payInfo'] = payInfo
        request.session['payTime'] = out_trade_no
        return_url = 'http://' + request.get_host() + '/shopper.html'
        url = get_pay(out_trade_no, total, return_url)
        return redirect(url)
    else:
        return redirect('shopper:shopcart')


