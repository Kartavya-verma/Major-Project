from django.db import models
#from django.contrib.auth.models import User

class InsuranceModel(models.Model):
    prod_info = models.DecimalField(max_digits=20,decimal_places=4)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=20,decimal_places=4)
    weight = models.DecimalField(max_digits=20,decimal_places=4)
    bmi = models.DecimalField(max_digits=20,decimal_places=4)
    employee = models.DecimalField(max_digits=20,decimal_places=4)
    insurance = models.DecimalField(max_digits=20,decimal_places=4)
    insurancehist1 = models.DecimalField(max_digits=20,decimal_places=4)
    insurancehist2= models.DecimalField(max_digits=20,decimal_places=4)
    family_his = models.DecimalField(max_digits=20,decimal_places=4)
    medical_his = models.DecimalField(max_digits=20,decimal_places=4)
    #risk_level = models.IntegerField(default=0)


    def __str__(self):
         return str(self.id)
