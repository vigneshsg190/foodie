from django.contrib import admin
from foodie.models import  products,usersignin,cartsaved,finalorder


class newclass(admin.ModelAdmin):
    list_display=('name','password','contact_num','address')

class productclass(admin.ModelAdmin):
    list_display=('product_name','price')

class  usrclass(admin.ModelAdmin):
    list_usr=('usrname','usrcontact_num','usraddress')

class  fiordrclass(admin.ModelAdmin):
    list_fi=('fiordid','cartid','usrid','prid','product_qty','total')


# Register your models here.

admin.site.register(usersignin,newclass)

admin.site.register(products,productclass)

admin.site.register(cartsaved)

admin.site.register(finalorder,fiordrclass)



