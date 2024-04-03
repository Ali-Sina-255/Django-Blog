from blogcatagory.models import Category

def get_categorys(reqeust):
    category = Category.objects.all()
    return dict(category=category)