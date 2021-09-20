from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserLogin(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput())


class UserReg(forms.ModelForm):
    number=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','password','email','number']

    def save(self, commit=True):
        user = super(UserReg, self).save(commit=False)
        user.number = self.cleaned_data["number"]
        if commit:
            user.save()
        return user
class Usearch(forms.Form):
    src=forms.CharField(max_length=50)
    des = forms.CharField(max_length=50)

class Trsc (forms.Form):
    tnum=forms.IntegerField()

class AddR(forms.Form):
    rid=forms.CharField(max_length=50)
    ostation=forms.CharField(max_length=50)
    dstation=forms.CharField(max_length=50)

class AddST(forms.Form):
    sid=forms.CharField(max_length=50)
    sname=forms.CharField(max_length=50)

class AddT(forms.Form):
    rid=forms.CharField(max_length=50)
    tno=forms.CharField(max_length=50)
    tname=forms.CharField(max_length=50)

class AddRT(forms.Form):
    tno=forms.CharField(max_length=50)
    sid= forms.CharField(max_length=50)
    rid=forms.CharField(max_length=50)
    order=forms.IntegerField()
    atime=forms.CharField(max_length=50)

class Pnr(forms.Form):
    pnr=forms.CharField(max_length=50)

class Book(forms.Form):
    cls=forms.CharField(max_length=10)
    dt=forms.CharField(max_length=10)
