from django.db import models
from django.contrib.auth.models import User

def frange(min, max, step):
    while min<=max:
        yield min
        min+=step

class Table(models.Model):
    MONTH_CHOICES = [ (str(round(i, 1)), str(round(i, 1))) for i in frange(0,1, 0.1) ]
    PERSENT = [ (str(i), str(i)) for i in range(0,101) ]
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, verbose_name='Пользователь', )
    A1 = models.CharField('A1 Число погибших результате ЧС на 100 000 человек', max_length=10, null=True, blank=True)
    A2 = models.IntegerField('A2 Число погибших в результате ЧС',null=True, blank=True,)
    A3 = models.IntegerField('A2 Число пострадавших в результате ЧС',null=True, blank=True,)
    B1 = models.CharField('B1 Число непосредственно пострадавших в результате ЧС на 100 000 человек', max_length=10, null=True, blank=True)
    B2 = models.CharField('B2 Число получивших увечья или пострадавших от болезней в результате ЧС на 100 000 человек',max_length=10, null=True, blank=True)
    B3 = models.IntegerField('B3 Число людей, жилища котоsрых были повреждены в результате ЧС',null=True, blank=True)
    B3a = models.IntegerField('B3a Число жилищ/домов, которые были повреждены в результате ЧС',null=True, blank=True)
    B4 = models.IntegerField('B4 Число людей, жилища которых были уничтожены в результате ЧС',null=True, blank=True)
    B4a = models.IntegerField('B4a Число жилищ/домов, которые были уничтожены в результате ЧС',null=True, blank=True)
    C1 = models.CharField('C1 Прямые экономические потери, связанные с бедствиями в отношении мирового валового внутреннего продукта (составной показатель)', max_length=10000000, null=True, blank=True)
    C2 = models.IntegerField('C2 Прямые потери в сельском хозяйстве, связанные с бедствиями.',null=True, blank=True)
    C3 = models.IntegerField('C3 Прямые экономические потери всех других поврежденных или разрушенных производственных активов, связанных с бедствиями. Производственные активы дезагрегированы по отраслям. Страны представляют доклады в отношении имеющихся секторов экономики.',null=True, blank=True)
    C4 = models.IntegerField('C4 Прямые экономические потери в жилищном секторе, связанные с бедствиями',null=True, blank=True)
    C5 = models.IntegerField('C5 Прямые экономические потери в результате повреждения или разрушения важнейших объектов инфраструктуры в результате ЧС',null=True, blank=True)
    C6 = models.IntegerField('C6 Прямые экономические потери в связи с повреждением или разрушением культурного наследия в результате ЧС',null=True, blank=True)
    G3 = models.CharField('G3 Число людей охваченных информационной системой раннего оповещения через местные органы власти или через национальные механизмы распространения информации на 100 000 человек', max_length=10, null=True, blank=True)
    G4 = models.IntegerField('G4 Доля местных органов власти, имеющих план действий в области раннего оповещения',null=True, blank=True)
    G5 = models.IntegerField('G5 Число стран, в которых население получает доступную, понятную, практическую и значимую информацию и оценки, касающиеся риска ЧС, на национальном и местном уровне',null=True, blank=True)
    G6a = models.CharField('G6a Доля населения, подверженного угрозе или риску ЧС, защита которого обеспечивается путем заблаговременной эвакуации на основе раннего оповещения', max_length=10, null=True, blank=True)
    G6a1 = models.IntegerField('G6a1 Число людей, защита которого обеспечивается путем заблаговременной эвакуации на основе экстренного оповещения',null=True, blank=True)
    G6a2 = models.IntegerField('G6a2 Численность населения, проживающего в зоне экстренного оповещения',null=True, blank=True)   
    E10 = models.CharField('E-1.1 Есть временные рамки, целевые задачи и индикатор / 2018',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E11 = models.CharField('E-1.1 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E12 = models.CharField('E-1.2 Задачи и меры, направленные на предотвращение создания риска / 2018',null=True, blank=True, max_length=32,  choices=MONTH_CHOICES)
    E13 = models.CharField('E-1.2 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E14 = models.CharField('E-1.3 Задачи и меры, направленные на снижение существующего риска / 2018',null=True, blank=True, max_length=32,  choices=MONTH_CHOICES)
    E15 = models.CharField('E-1.3 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E16 = models.CharField('E-1.4 Задачи и меры, направленные на укрепление экономической, социальной, санитарной и экологической устойчивости / 2018',null=True, blank=True, max_length=32,  choices=MONTH_CHOICES)
    E17 = models.CharField('E-1.4 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E18 = models.CharField('E-1.5 Рассмотрите рекомендации Приоритета 1, Понимание риска бедствий / 2018',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E19 = models.CharField('E-1.5 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E20 = models.CharField('E-1.6 Рассмотрите рекомендации Приоритета 2, Укрепление управления рисками стихийных бедствий для управления рисками бедствий / 2018',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E21 = models.CharField('E-1.6 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E22 = models.CharField('E-1.7 Рассмотрите рекомендации Приоритета 3, Инвестиции в снижение риска бедствий для обеспечения устойчивости / 2018',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E23 = models.CharField('E-1.7 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E24 = models.CharField('E-1.8 Удовлетворение рекомендаций Приоритета 4, Повышение готовности к стихийным бедствиям для эффективного реагирования и «Улучшение / 2018', null=True, blank=True,  max_length=32, choices=MONTH_CHOICES)
    E25 = models.CharField('E-1.8 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E26 = models.CharField('E-1.9 Содействовать обеспечению согласованности политики и её соблюдения, в частности, с Целями Устойчивого Развития и Парижским соглашением / 2018',null=True, blank=True,max_length=32,  choices=MONTH_CHOICES)
    E27 = models.CharField('E-1.9 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E28 = models.CharField('E-1.10 Имеются механизмы для последующей деятельности, периодически оценивать и публично сообщать о прогрессе / 2018',null=True, blank=True, max_length=32,  choices=MONTH_CHOICES)   
    E29 = models.CharField('E-1.10 2017',null=True, blank=True, max_length=32, choices=MONTH_CHOICES)
    E30 = models.CharField('E-2.1 Имеет цели и меры направленные на снижение существующего риска',null=True, blank=True, max_length=4, choices=PERSENT )
    E31 = models.CharField('E-2.2 Имеет цели и меры направленные на предотвращение появления риска задачи, индикаторы',null=True, blank=True, max_length=4, choices=PERSENT)
    E32 = models.CharField('E-2.3 Имеет цели и меры направленные на укрепление экономической, социальной, экологической устойчивости и устойчивости здравоохранения',null=True, blank=True, max_length=4, choices=PERSENT)
    E33 = models.CharField('E-2.4 Имеет временные рамки, цели и индикаторы',null=True, blank=True, max_length=4, choices=PERSENT)
    E34 = models.CharField('E-2.5 Выполняет рекомендации и предложения Приоритета 1 «Понимание риска бедствий» ',null=True, blank=True, max_length=4, choices=PERSENT)
    E35 = models.CharField('E-2.6 Выполняет рекомендации и предложения Приоритета 2 «совершенствование организационно-правовых рамок управления риском бедствий»',null=True, blank=True, max_length=4, choices=PERSENT)
    E36 = models.CharField('E-2.7 Выполняет рекомендациии предложения Приоритета 3 «Инвестиции в меры по снижению риска бедствий в целях укрепления потенциала противодействия»',null=True, blank=True, max_length=4, choices=PERSENT)
    E37 = models.CharField('E-2.8 Выполняет рекомендации и предложения Приоритета 4 «Повышение готовности к бедствиям для обеспечения эффективного реагирования и внедрение принципа «сделать лучше, чем было» в деятельность по восстановлению, реабилитации и реконструкции» ',null=True, blank=True, max_length=4, choices=PERSENT)
    E38 = models.CharField('E-2.9 Интегрирована на всех уровнях по развитию и планам и политике по искоренению бедности, в особенности ЦУР',null=True, blank=True, max_length=4, choices=PERSENT)
    E39 = models.CharField('E-2.10 Продвигает единение, интеграцию и соответствие планов адаптации к ИК и смягчения его последствий, в соответствии с Парижским ',null=True, blank=True, max_length=4, choices=PERSENT)

class regionchoise(models.Model):
    region = models.CharField('Введите регион',null=False,blank=True, unique=True, max_length=200,)
    
    def __str__(self):
        return self.region

class Usersdate(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, verbose_name='Пользователь',)
    region = models.OneToOneField(regionchoise, on_delete=models.CASCADE, blank=True, verbose_name='Выберите регион',)
    vrp = models.IntegerField('Введите ВВР', null=True, blank=True, )
    people = models.IntegerField('ВВедиет численность населения', null=True, blank=True,)

