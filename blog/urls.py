#_*_coding:UTF-8_*_
#开发团队:木木
#开发人员:Administrator
#开发时间: 9:37
#文件名称:urls.PY
#开发工具:pycharm
from django.urls import path

from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]