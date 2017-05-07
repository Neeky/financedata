from django.db import models

# Create your models here.
class ShiborRate(models.Model):
    """
    ShiborRate用来保存shibor利率的相关数据
    pushDate    --  利率发布的时间日期
    oneNight    --  隔离利率
    oneWeek     --  一周期利率
    twoWeek     --  两周期利率
    oneMonth    --  一月期利率
    twoMonth    --  两月期利率
    threeMonth  --  三月期利率
    sixMonth    --  半年期利率
    nineMonth   --  九月期利率
    oneYear     --  一年期利率
    """
    pushDate=models.DateTimeField(primary_key=True)
    oneNight=models.DecimalField(max_digits=10,decimal_places=6)
    oneWeek=models.DecimalField(max_digits=10,decimal_places=6)
    twoWeek=models.DecimalField(max_digits=10,decimal_places=6)
    oneMonth=models.DecimalField(max_digits=10,decimal_places=6)
    threeMonth=models.DecimalField(max_digits=10,decimal_places=6)
    sixMonth=models.DecimalField(max_digits=10,decimal_places=6)
    nineMonth=models.DecimalField(max_digits=10,decimal_places=6)
    oneYear=models.DecimalField(max_digits=10,decimal_places=6)