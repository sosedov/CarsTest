from django.db import models

class cars_label(models.Model):
    name = models.CharField(verbose_name="марка авто", max_length=64)
    country = models.CharField(verbose_name="страна производителя", max_length=64)




