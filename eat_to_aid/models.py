from django.db import models
import uuid
class CoupounModel(models.Model):
    name = models.CharField(max_length=300)
    shop= models.ForeignKey("ShopModel",on_delete=models.RESTRICT)
    discount= models.FloatField()

    def __str__(self) -> str:
        return self.name

class ShopModel(models.Model):
    name = models.CharField(max_length=300)
    lattitude= models.FloatField()
    longitude =models.FloatField()
    address =models.CharField(max_length=800)
    menu =models.CharField(max_length=800)

    def __str__(self) -> str:
        return self.name
    
