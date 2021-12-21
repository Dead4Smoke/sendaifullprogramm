from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q 


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

@login_required
def main(request):
    autodok = Table.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
            #Сохранение с пользователем
        post_data = request.body.decode('utf-8').split("&")
            ###
        form = TableForm(request.POST)
        man = Usersdate.objects.get(User=request.user)
        l = man.people
        vrp = man.vrp
        if form.is_valid():
            try:
                old_form = Table.objects.get(User=request.user)
                old_form.delete()
            except Table.DoesNotExist as e:
                pass
            ###New
            instance = form.save(commit=False)
            instance.User = request.user
            b = instance.A2
            t = instance.A3
            s = (b/l)
            d = (t/l)
            instance.A1 = toFixed(s, 6)
            instance.B1 = toFixed(d, 6)
            instance.B2 = toFixed(d, 6) 
            instance.G3 = toFixed(s, 6)
            g6a1 = instance.G6a1
            g6a2 = instance.G6a2  
            instance.G6a = (g6a1/g6a2)
            b = instance.A2
            c2 = instance.C2
            c3 = instance.C3
            c4 = instance.C4
            c5 = instance.C5
            c6 = instance.C6
            c0 = (c2+c3+c4+c5+c6)
            c1 = (c0/vrp)
            instance.C1 = toFixed(c1, 6) 
            print(instance.C1)      
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
        else:
            messages.success(request, 'Заполните поля правильно!')

    #автозаполнение
    form = TableForm(instance=autodok)
    is_exist = False
    try:
        Table.objects.get(User=request.user)
        is_exist = True
    except:
        pass               
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist
        }
    return render(request, 'base/main.html', data)

@login_required   
def start(request):
    autodok = Usersdate.objects.filter(User=request.user).first()
    error = ''
    if request.method == 'POST':
            #Сохранение с пользователем
        #post_data = request.body.decode('utf-8').split("&")
            ###
        form = UsersdateForm(request.POST)
        if form.is_valid():
            try:
                old_form = Usersdate.objects.get(User=request.user)
                old_form.delete()
            except Usersdate.DoesNotExist as e:
                pass
            ###New
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            ###
            messages.success(request, 'Ваши данные отправлены на проверку')
            return redirect('main')
        else:
            messages.success(request, 'Заполните поля правильно!')
    form = UsersdateForm(instance=autodok)
    is_exist = False
    try:
        Usersdate.objects.get(User=request.user)
        is_exist = True
    except:
        pass        
    data = {
        'form' : form,
        'error': error,
        'is_exist': is_exist
        }
    return render(request, 'base/start.html', data)

@login_required  
def report(request):
    RepA1 = Table.objects.aggregate(Sum('A1'))
    RepA2 = Table.objects.aggregate(Sum('A2'))
    RepB1 = Table.objects.aggregate(Sum('B1'))
    RepB2 = Table.objects.aggregate(Sum('B2'))
    RepB3 = Table.objects.aggregate(Sum('B3'))
    RepB4 = Table.objects.aggregate(Sum('B3a'))
    RepB5 = Table.objects.aggregate(Sum('B4'))
    RepB6 = Table.objects.aggregate(Sum('B4a'))
    RepC1 = Table.objects.aggregate(Sum('C1'))
    RepC2 = Table.objects.aggregate(Sum('C2'))
    RepC3 = Table.objects.aggregate(Sum('C3'))
    RepC4 = Table.objects.aggregate(Sum('C4'))
    RepC5 = Table.objects.aggregate(Sum('C5'))
    RepC6 = Table.objects.aggregate(Sum('C6'))
    RepG3 = Table.objects.aggregate(Sum('G3'))
    RepG4 = Table.objects.aggregate(Sum('G4'))
    RepG5 = Table.objects.aggregate(Sum('G5'))
    RepG6 = Table.objects.aggregate(Sum('G6a'))
    RepG7 = Table.objects.aggregate(Sum('G6a1'))
    RepG8 = Table.objects.aggregate(Sum('G6a2'))
    RepE10 = Table.objects.aggregate(Sum('E10'))
    RepE11 = Table.objects.aggregate(Sum('E11'))
    RepE12 = Table.objects.aggregate(Sum('E12'))
    RepE13 = Table.objects.aggregate(Sum('E13'))
    RepE14 = Table.objects.aggregate(Sum('E14'))
    RepE15 = Table.objects.aggregate(Sum('E15'))
    RepE16 = Table.objects.aggregate(Sum('E16'))
    RepE17 = Table.objects.aggregate(Sum('E17'))
    RepE18 = Table.objects.aggregate(Sum('E18'))
    RepE19 = Table.objects.aggregate(Sum('E19'))
    RepE20 = Table.objects.aggregate(Sum('E20'))
    RepE21 = Table.objects.aggregate(Sum('E21'))
    RepE22 = Table.objects.aggregate(Sum('E22'))
    RepE23 = Table.objects.aggregate(Sum('E23'))
    RepE24 = Table.objects.aggregate(Sum('E24'))
    RepE25 = Table.objects.aggregate(Sum('E25'))
    RepE26 = Table.objects.aggregate(Sum('E26'))
    RepE27 = Table.objects.aggregate(Sum('E27'))
    RepE28 = Table.objects.aggregate(Sum('E28'))
    RepE29 = Table.objects.aggregate(Sum('E29'))
    Rep = {  
            'RepA1': RepA1,
            'RepA2': RepA2,
            'RepB1': RepB1,
            'RepB2': RepB2,
            'RepB3': RepB3,
            'RepB4': RepB4,
            'RepB5': RepB5,
            'RepB6': RepB6,
            'RepC1': RepC1,
            'RepC2': RepC2,
            'RepC3': RepC3,
            'RepC4': RepC4,
            'RepC5': RepC5,
            'RepC6': RepC6,
            'RepG3': RepG3,
            'RepG4': RepG4,
            'RepG5': RepG5,
            'RepG6': RepG6,
            'RepG7': RepG7,
            'RepG8': RepG8,
            'RepE10': RepE10,
            'RepE11': RepE11,
            'RepE12': RepE12,
            'RepE13': RepE13,
            'RepE14': RepE14,
            'RepE15': RepE15,
            'RepE16': RepE16,
            'RepE17': RepE17,
            'RepE18': RepE18,
            'RepE19': RepE19,
            'RepE20': RepE20,
            'RepE21': RepE21,
            'RepE22': RepE22,
            'RepE23': RepE23,
            'RepE24': RepE24,
            'RepE25': RepE25,
            'RepE26': RepE26,
            'RepE27': RepE27,
            'RepE28': RepE28,
            'RepE29': RepE29,
        }
    return render(request, 'base/report.html', Rep)
  
@login_required
def panel(request):  
    table = None
    try: 
        table = Table.objects.get(User=request.user)  
    except:
        pass
    if table:
        return render(request, 'base/panel.html', {"table": table})  
    else:
        messages.success(request, 'Вы не отправили данные')
        return render(request,'base/panel.html')
   
@login_required
def region(request):
    table = Table.objects.all()
    form = UsersdateForm(request.POST)
    region = {
        'table': table,
        'form': form,
    }
    return render(request, 'base/region.html', {'region': region})
 
class SearchResultsView(ListView):
    model = Table
    template_name = 'base/search.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('region')
        users = Usersdate.objects.filter(region=query)
        tables = []
        for user in users:
            table = Table.objects.filter(User=user.User).first()
            if table:
                table.Usersdate = user
                tables.append(table)
        return tables  
