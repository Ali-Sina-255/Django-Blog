from django.forms import ModelForm
from blogcatagory.models import Category, Blog


class AddCategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"