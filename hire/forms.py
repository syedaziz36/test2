from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from .models import *



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']



class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile1
		fields = ['skills','stackoverflow_link','codechef_link','techgig_link','codeforces_link', 'profile_pic', 'tag_line']


class CompanyProfileForm(forms.ModelForm):
	class Meta:
		model = CompanyProfile
		fields = ['company_name','company_id','company_logo', 'company_link']