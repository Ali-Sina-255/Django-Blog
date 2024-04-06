from django.forms import ModelForm
from blogcatagory.models import Category, Blog


class AddCategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
    
class AddPostForms(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['slug', 'author']