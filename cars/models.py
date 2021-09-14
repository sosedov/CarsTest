from django.db import models

class CarsLabel(models.Model):
    name = models.CharField(verbose_name="Model", max_length=64)
    country = models.CharField(verbose_name="Country", max_length=64)




