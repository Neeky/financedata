from django.shortcuts import render
from django.views import View
"""
完成shibor利率项目相关的后台处理.
"""


# Create your views here.
class ShiborGather(View):
    """
    对shibor的所有处理都交由这个类来完成.
    """
    def post(self,request):
        """
        接收由shiborClient post上来的数据、并把数据保存到数据库中。
        """


