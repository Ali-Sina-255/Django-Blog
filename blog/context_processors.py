from blogcatagory.models import Category
from social.models import SocialLink

def get_categorys(reqeust):
    category = Category.objects.all()
    return dict(category=category)


def get_social_links(reqeust):
    social_link = SocialLink.objects.all()
    return dict(social_link=social_link)