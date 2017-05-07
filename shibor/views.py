from django.shortcuts import render
from django.views import View
from .models import ShiborRate
from django.http import HttpResponse,JsonResponse
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
        返回json对象、statuCode用来表示成功与否、msg用来表示详细的内容。
        """
        try:
            shibor=ShiborRate()
            shibor.pushDate=request.POST['pushDate']
            shibor.oneNight=request.POST['oneNight']
            shibor.oneWeek=request.POST['oneWeek']
            shibor.twoWeek=request.POST['twoWeek']
            shibor.oneMonth=request.POST['oneMonth']
            shibor.threeMonth=request.POST['threeMonth']
            shibor.sixMonth=request.POST['sixMonth']
            shibor.nineMonth=request.POST['nineMonth']
            shibor.oneYear=request.POST['oneYear']
            shibor.save()
            return JsonResponse({'statuCode':0,'msg':'OK'})
        except Exception as e:
            print(e)
            return JsonResponse({'statuCode':100,'msg':str(e)})




