"""babys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,re_path,include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #添加项目应用index,commodity和shopper的urls.py
    path('',include(('index.urls','index'),namespace='index')),
    path('commodity',include(('commodity.urls','commodity'),namespace='commodity')),
    path('shopper',include(('shopper.urls','shopper'),namespace='shopper')),

    #配置媒体资源的路由信息 这样就可以在开发阶段直接使用静态文件了。
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # 定义静态资源的路由信息
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static'),


]
# 设置404和500
from index import views
handler404 = views.page_not_found
handler500 = views.page_error