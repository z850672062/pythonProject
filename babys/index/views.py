#项目应用index的views.py
from django.shortcuts import render
from django.views.generic.base import TemplateView
from commodity.models import *
# Create your views here.

# def indexView(request):
#     #网页标签内容，即HTML的title标签文本内容，该变量将会在模板中使用
#     title = '首页'
#     #类内容，控制网页导航栏的样式
#     classContent = ''
#     #从0到8的sold降序排列
#     commodityInfos = CommodityInfos.objects.order_by('-sold').all()[:8]
#     #types是查询模型Types的所有数据
#     types = Types.objects.all()
#
#     #宝宝服饰
#     cl = [x.seconds for x in types if x.firsts == '儿童服饰']
#     clothes = CommodityInfos.objects.filter(types__in = cl).order_by('-sold')[:5]
#
#     #奶粉辅食
#     fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
#     food = CommodityInfos.objects.filter(types__in = fl).order_by('-sold')[:5]
#
#     #宝宝用品
#     gl = [x.seconds for x in types if x.firsts == '儿童用品']
#     goods = CommodityInfos.objects.filter(types__in = gl).order_by('-sold')[:5]
#
# # locals()为
#     return render(request,'index.html',locals())


class indexClassView(TemplateView):
    #设置模板文件名，网页内容由模板文件index.html生成
    template_name = 'index.html'
    #设置解析模板文件的模板引擎，属性值为None则默认使用配置文件settings.py的TEMPLATES的BACKEND所设置的模板引擎
    template_engine = None
    #属性content_type设置响应内容的数据格式，属性值为None则使用text/html作为响应内容的数据格式
    content_type = None
    #属性extra_context为模板文件设置额外变量。
    extra_context = {'titel':'首页','classContent':''}

    #重新定义模板上下文的获取方式
    #方法get_context_data是获取属性extra_context的值，如果某些变量具有动态变化或者需要复杂的处理逻辑，可以在此方法里面动态添加这些变量，比如查询模型数据
    #数据的算法处理等。
    def get_context_data(self, **kwargs):
        #super() 函数是用于调用父类(超类)的一个方法。
        context = super().get_context_data(**kwargs)
        context['commodityInfos'] = CommodityInfos.objects.order_by('-sold').all()[:8]
        types = Types.objects.all()

        # 宝宝服饰
        cl = [x.seconds for x in types if x.firsts == '儿童服饰']
        context['clothes'] = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]

        # 奶粉辅食
        fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
        context['food'] = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]

        # 宝宝用品
        gl = [x.seconds for x in types if x.firsts == '儿童用品']
        context['goods'] = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]

        return context

    #定义HTTP的GET请求处理方法
    #参数request代表HTTP请求信息
    #若路由设有路由变量，则可从参数kwargs里获取
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    #定义HTTP的POST请求处理方法
    #参数request代表HTTP请求信息
    #若路由设有路由变量，则可从参数kawrgs里获取
    def post(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)



