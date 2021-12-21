from .models import *
from django.forms import *

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = [
        'A1','A2','A3',
        'B1','B2','B3','B3a','B4','B4a',
        'C1','C2','C3','C4','C5','C6',
        'G3','G4','G5','G6a','G6a1','G6a2',
        'User',
        'E10','E11','E12','E13','E14','E15','E16','E17','E18','E19',
        'E20','E21','E22','E23','E24','E25','E26','E27','E28','E29',
        'E30','E31','E32','E33','E34','E35','E36','E37','E38','E39'
        ]
        widgets = {  
            "A1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "A3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "B1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "B2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "B3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "B3a": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "B4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "B4a": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "C1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "C2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "C3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "C4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "C5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "C6": TextInput(attrs={'class': 'form-control','type': 'text',}),    
            "G1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G3": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G4": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G5": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G6a": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G6a1": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "G6a2": TextInput(attrs={'class': 'form-control','type': 'text',}),
            "User": Select(attrs={'class': 'form-control2','type': 'text',}),
            "E10": Select(attrs={'class': 'form-control','type': 'text',}),
            "E11": Select(attrs={'class': 'form-control','type': 'text',}),
            "E12": Select(attrs={'class': 'form-control','type': 'text',}),
            "E13": Select(attrs={'class': 'form-control','type': 'text',}),
            "E14": Select(attrs={'class': 'form-control','type': 'text',}),
            "E15": Select(attrs={'class': 'form-control','type': 'text',}),
            "E16": Select(attrs={'class': 'form-control','type': 'text',}),
            "E17": Select(attrs={'class': 'form-control','type': 'text',}),
            "E18": Select(attrs={'class': 'form-control','type': 'text',}),
            "E19": Select(attrs={'class': 'form-control','type': 'text',}),
            "E20": Select(attrs={'class': 'form-control','type': 'text',}),
            "E21": Select(attrs={'class': 'form-control','type': 'text',}),
            "E22": Select(attrs={'class': 'form-control','type': 'text',}),
            "E23": Select(attrs={'class': 'form-control','type': 'text',}),
            "E24": Select(attrs={'class': 'form-control','type': 'text',}),
            "E25": Select(attrs={'class': 'form-control','type': 'text',}),
            "E26": Select(attrs={'class': 'form-control','type': 'text',}),
            "E27": Select(attrs={'class': 'form-control','type': 'text',}),
            "E28": Select(attrs={'class': 'form-control','type': 'text',}),
            "E29": Select(attrs={'class': 'form-control','type': 'text',}), 
            "E30": Select(attrs={'class': 'form-control','type': 'text',}),
            "E31": Select(attrs={'class': 'form-control','type': 'text',}),
            "E32": Select(attrs={'class': 'form-control','type': 'text',}),
            "E33": Select(attrs={'class': 'form-control','type': 'text',}),
            "E34": Select(attrs={'class': 'form-control','type': 'text',}),
            "E35": Select(attrs={'class': 'form-control','type': 'text',}),
            "E36": Select(attrs={'class': 'form-control','type': 'text',}),
            "E37": Select(attrs={'class': 'form-control','type': 'text',}),
            "E38": Select(attrs={'class': 'form-control','type': 'text',}),
            "E39": Select(attrs={'class': 'form-control','type': 'text',}), 
        }

class UsersdateForm(ModelForm):
    class Meta:
        model = Usersdate
        fields = [
        'region', 'vrp', 'people', 'User'  
        ]
        widgets = {
            "region": Select(attrs={'class':'form-control','type': 'text',}),
            "vrp": TextInput(attrs={'class':'form-control','type': 'text',}),
            "people": TextInput(attrs={'class':'form-control','type': 'text',}),
            "User": Select(attrs={'class': 'form-control2','type': 'text',}),
        }
