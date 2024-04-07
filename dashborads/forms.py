from django import forms
from blogcatagory.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

class AddCategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
    
class AddPostForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['slug', 'author']
        
        
class UserCreationForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'is_active', 'is_staff','is_superuser','groups','user_permissions']
        
class Edit_UserFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'is_active', 'is_staff','is_superuser','groups','user_permissions']
        