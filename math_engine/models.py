from django.db import models

class MathRequest(models.Model):
    ip = models.IPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    values = models.CharField(max_length=512)
    sum = models.IntegerField()
    product = models.IntegerField()
