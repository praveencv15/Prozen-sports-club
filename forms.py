from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Member_details, Store, TournamentRegistration

INPUT_CLASSES = 'w-3/4 py-4 px-6 rounded-xl border mr-5 ml-5'

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your Username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Member_details
        fields = ('firstname','lastname','gender', 'passport','PlayerType','RunsScored')
        widgets = {
            'firstname' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'lastname' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gender' : forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'PlayerType' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'RunsScored' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'passport' : forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

    }
        
class NewStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('item_name', 'photo', 'price', 'stock_available')
        widgets = {
            'item_name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'photo' : forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'stock_available' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
class TournamentRegistrationForm(forms.ModelForm):
    class Meta:
        model = TournamentRegistration
        fields = ['name', 'sport', 'contact', 'date', 'location']  
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'sport': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'contact': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'date': forms.DateInput(attrs={'class': INPUT_CLASSES, 'type': 'date'}), 
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES}),  
        }

    
