from django.shortcuts import render, redirect
import joblib
from app.forms import InsuranceForm, CustomerRegistrationForm
from django.views import View
from django.contrib import messages
import random
from app.models import InsuranceModel


def home(request):
    fm = InsuranceForm()
    return render(request,'app/home.html', {'form': fm})


def index(request):
    return render(request, 'app/index.html')


def result(request):
    if request.method == 'POST':
        cls = joblib.load('finalized_model.sav')
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            lis = []
            lis.append(form.cleaned_data['prod_info'])
            lis.append(form.cleaned_data['age'])
            lis.append(form.cleaned_data['height'])
            lis.append(form.cleaned_data['weight'])
            lis.append(form.cleaned_data['bmi'])
            lis.append(form.cleaned_data['employee'])
            lis.append(form.cleaned_data['insurance'])
            lis.append(form.cleaned_data['insurancehist1'])
            lis.append(form.cleaned_data['insurancehist2'])
            lis.append(form.cleaned_data['family_his'])
            lis.append(form.cleaned_data['medical_his'])

            #ans = cls.predict([[0.076923,	0.059701,	0.600000,	0.131799,	0.272288,	0.000,	6.0,	1.0,	0.000133,	2.0,	5.000000]])
            #ans = cls.predict([lis])
            #ID_S = InsuranceModel.objects.order_by('id').last()
            #print(InsuranceModel.objects.filter(id=ID_S))
            ans = sum(lis)
            if ans <= 200:
                #if(InsuranceModel[risk_level]'==0):
                level = random.randint(1,7)
                print(level)
                #Insu = InsuranceModel.objects.filter()
                return redirect('/accept')
            else:
                return redirect('/reject')

    else:
        print("empty")
        form = InsuranceForm()
        return render(request, 'app/home.html', {'form': form})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/registration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/registration.html', {'form': form})


def profile(request):
    return render(request, 'app/profile.html')


def accept(request):
    level = random.randint(1,7)
    random.seed(10)
    return render(request, 'app/accept.html', {'risk': level})


def reject(request):
    return render(request, 'app/reject.html', {'risk': 8})


def premium(request):
    level = random.randint(1,7)
    random.seed(10)
    return render(request, 'app/premium.html', {'risk': level})
