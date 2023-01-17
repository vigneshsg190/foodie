
from django.db import models

# Create your models here.
class usersignin(models.Model):
    usrid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contact_num=models.CharField(max_length=100)
    address=models.CharField(max_length=100)  

    class Meta:
        db_table="usersignintable"
class products(models.Model):
    prid=models.AutoField(primary_key=True,default=True)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.CharField(max_length=2500, null=True)

    

class cartsaved(models.Model):
    cartid=models.AutoField(primary_key=True) 
    usrid=models.ForeignKey(usersignin,on_delete=models.DO_NOTHING,blank=True,null=True)
    prid=models.ForeignKey(products,on_delete=models.DO_NOTHING,null=True)
    product_qty=models.IntegerField()
    status=models.BooleanField(default=False)
    total=models.IntegerField(null=False)
    created_at=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table="cartsaved"


class finalorder(models.Model):
    fiordid=models.AutoField(primary_key=True) 
    cartid=models.ForeignKey(cartsaved,on_delete=models.DO_NOTHING,blank=True,null=True) 
    usrid=models.ForeignKey(usersignin,on_delete=models.DO_NOTHING,blank=True,null=True)
    prid=models.ForeignKey(products,on_delete=models.DO_NOTHING,null=True)
    product_qty=models.IntegerField()
    total=models.IntegerField(null=False)
    status=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)

    class Meta:
        db_table="finalorder"        
     





    




            
            