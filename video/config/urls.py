# coding:utf-8
from django.contrib import admin
from django.urls import path, include
from app.dashboard import urls as dashboard_urls
from app.client import urls as client_urls


#include()即把这里面的urlpatterns全部导进来

urlpatterns = [
    # 这个用不着
    # path('admin/', admin.site.urls),
    path('dashboard/', include(dashboard_urls)),
    path('client/', include(client_urls))
    # 访问就是 client/client_urls
]
