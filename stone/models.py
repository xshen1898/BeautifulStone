from django.db import models

# Create your models here.
class Lottery(models.Model):
    cellphone_num = models.CharField(max_length=50)
    award = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cellphone_num