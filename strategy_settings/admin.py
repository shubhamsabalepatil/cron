from django.contrib import admin
from .models import Strategy_details,Strategy_Parameters, Add_Symbol, Add_Instance

# Register your models here.

class Admin_Strategy_details(admin.ModelAdmin):
    fields = ['Name','Code','Time_Frame','Type','Initialize_Time','Script']
    model = Strategy_details


admin.site.register(Strategy_details, Admin_Strategy_details)

class Admin_Strategy_Parameters(admin.ModelAdmin):
    fields = ['Strategy','Name','Descrption','Variable_Name','Parameter_Type','Parameter_Value']
    model = Strategy_Parameters


admin.site.register(Strategy_Parameters, Admin_Strategy_Parameters)



class Admin_Symbol(admin.ModelAdmin):
    fields = ['strategy','Exchange','Symbol','is_Monday','is_Tuesday','is_Wednesday','is_Thursday','is_Friday']
    model = Add_Symbol


admin.site.register(Add_Symbol, Admin_Symbol)


class Admin_Instance(admin.ModelAdmin):
    fields = ['Strategy','Exchange','Symbol','is_Monday','is_Tuesday','is_Wednesday','is_Thursday','is_Friday','Initialize_Time','Terminate_Time']
    model = Add_Instance

admin.site.register(Add_Instance, Admin_Instance)








