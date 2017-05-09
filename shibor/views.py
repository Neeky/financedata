from django.shortcuts import render
from django.views import View
from .models import ShiborRate
from django.http import HttpResponse,JsonResponse
from datetime import datetime
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



class ShiborReport(View):
    """
    导出shibor利率的报表数据
    
    """
    #all 表示所有期限.
    terms=['oneNight','oneWeek','twoWeek','oneMonth','threeMonth','sixMonth','nineMonth','oneYear','all']
    def getOneNight(self,termName,fromDate,toDate):
        """
        完成对隔夜利率的抽取
        ternName        --  期限名
        fromDate        --  起始日期、datetime类型
        toDate          --  截止日期、toDate类型
        """
        return ShiborRate.objects.values('pushDate','oneNight').filter(pushdate__gte=fromDate).filter(pushDate__lte=toDate)

    def post(self,request):
        """
        --实现报表的接口   ...
        request.POST字典要包涵如下三个字段
        term        --  期限  {'oneNight','oneWeek','twoWeek','oneMonth','threeMonth','sixMonth','nineMonth','oneYear',all}
        fromDate    --  起始日期、格式为:yyyy-mm-dd
        toDate          --  截止日期、格式为:yyyy-mm-dd
        
        1:完成对请求参数的验证
        2:抽取数据
        3:按定义好的格式返回

        返回的json格式{
            'msg':'xxx'
            'data':[]
        }
        """
        result={}
        result['msg']='OK'
        #:第一步、参数验证
        try:
            #取参数的值 \如果取不到就会引发KeyError
            term=request.POST['term']
            fromDate=request.POST['fromDate']
            toDate=request.POST['toDate']

            #对参数值进行转换 \如果值的格式不对会引发ValueError
            year,month,day=fromDate.split('-')
            fromDate=datetime(year=int(year),month=int(month),day=int(day))
            year,month,day=toDate.split('-')
            toDate=datetime(year=int(year),month=int(month),day=int(day),hour=23,minute=59,sencond=59)
            if term not in ShiborReport.terms:
                raise ValueError("{0}这个值对于shiborReport来说不正确")
            
            #抽数据
            data=self.getOneNight(termName,fromDate,toDate)
            result['datas']=[{'oneNight':data},]

            #返回数据
            return JsonResponse(result)

        except KeyError as e:
            result['msg']=str(e)
            return JsonResponse(result)
        except ValueError as e:
            result['msg']=str(e)
            return JsonResponse(result)
        except Exception as e:
            result['msg']=str(e)
            return JsonResponse(result)