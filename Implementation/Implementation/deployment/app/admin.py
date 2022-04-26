from django.contrib import admin
from .models import InsuranceModel

# Register your models here.
@admin.register(InsuranceModel)
class InsuranceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod_info', 'age', 'height', 'weight', 'bmi', 'employee', 'insurance', 'insurancehist1', 'insurancehist2', 'family_his', 'medical_his')
