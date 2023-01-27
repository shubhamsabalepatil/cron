from django.db import models

# Create your models here.


Time_Frame_Choise=(
    ("Intraday","Intraday"),
    ("Positional","Positional")
)

Type_Choise =(
    ("Short Volatility","Short Volatility"),
    ("Short Directional","Short Directional"),
    ("Long Directional","Long Directional"),
    ("Pattern System","Pattern System"),
    ("Calendar Spread","Calendar Spread"),
    ("Expiry","Expiry"),
)

class Strategy_details(models.Model):
    Name = models.CharField(max_length=30)
    Code = models.CharField(max_length=30)
    Time_Frame = models.CharField(max_length=30,choices = Time_Frame_Choise)
    Type = models.CharField(max_length=30,choices=Type_Choise)
    Initialize_Time = models.TimeField()
    Script = models.CharField(max_length=30)

Parameter_Type_Choice = [
    ("Number", "Number"),
    ("Time", "Time")
    ]


class Strategy_Parameters(models.Model):
    Strategy = models.ForeignKey(Strategy_details, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Descrption = models.CharField(max_length=200)
    Variable_Name = models.CharField(max_length=30)
    Parameter_Type = models.CharField(max_length=30, choices=Parameter_Type_Choice)
    Parameter_Value = models.CharField(max_length=10, default="")

Exchange_Choice = (
    ('NSE','NSE'),
    ('BSE','BSE')
)

Symbol_Choice = (
    ('A','A'),
    ('B','B'),
    ('C','C')
)


class Add_Symbol(models.Model):
    strategy = models.ForeignKey(Strategy_details, on_delete=models.CASCADE)
    Exchange = models.CharField(max_length=30,choices=Exchange_Choice)
    Symbol = models.CharField(max_length=30, choices=Symbol_Choice)
    is_Monday = models.BooleanField("Monday",default=False)
    is_Tuesday = models.BooleanField("Tuesday",default=False)
    is_Wednesday = models.BooleanField("Wednesday",default=False)
    is_Thursday = models.BooleanField("Thursday",default=False)
    is_Friday = models.BooleanField("Friday",default=False)

Exchange_Choice = (
    ('NSE','NSE'),
    ('BSE','BSE')
)

Symbol_Choice = (
    ('A','A'),
    ('B','B'),
    ('C','C')
)

class Add_Instance(models.Model):
    Strategy = models.ForeignKey(Strategy_details,on_delete=models.CASCADE)
    Exchange = models.CharField(max_length=30,choices=Exchange_Choice)
    Symbol = models.CharField(max_length=30, choices=Symbol_Choice)
    is_Monday = models.BooleanField("Monday", default=False)
    is_Tuesday = models.BooleanField("Tuesday", default=False)
    is_Wednesday = models.BooleanField("Wednesday", default=False)
    is_Thursday = models.BooleanField("Thursday", default=False)
    is_Friday = models.BooleanField("Friday", default=False)
    Initialize_Time = models.TimeField()
    Terminate_Time = models.TimeField()