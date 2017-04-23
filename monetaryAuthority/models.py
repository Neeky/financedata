from django.db import models

# Create your models here.

# 针对中国人民银行的统计数据进行建模

class MoneySupply(models.Model):
    """货币供应量"""
    yearMonth=models.DateField()
    m0=models.FloatField()
    m1=models.FloatField()
    m2=models.FloatField()


