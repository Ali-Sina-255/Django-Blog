from django.forms import ModelForm
from blogcatagory.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddCategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
    
class AddPostForms(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['slug', 'author']
        
        
class UserCreationForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']