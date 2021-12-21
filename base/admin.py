from django.contrib import admin
from .models import *

class TableAdmin(admin.ModelAdmin):
    list_display = (
        'User',
        'A1','A2','A3',
        'B1','B2','B3','B3a','B4','B4a',
        'C1','C2','C3','C4','C5','C6',
        'G3','G4','G5','G6a','G6a1','G6a2',
        'E10','E11','E12','E13','E14','E15','E16','E17','E18','E19',
        'E20','E21','E22','E23','E24','E25','E26','E27','E28','E29',
        'E30','E31','E32','E33','E34','E35','E36','E37','E38','E39'
        )
admin.site.register(Table, TableAdmin)

class UsersdateAdmin(admin.ModelAdmin):
    list_display = (
        'User','region','vrp','people',
        )
admin.site.register(Usersdate, UsersdateAdmin)

class regionAdmin(admin.ModelAdmin):
    list_display = (
        'region',
        )
admin.site.register(regionchoise, regionAdmin)


