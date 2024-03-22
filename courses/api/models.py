from shop.models import Category, Course
from tastypie.resources import ModelResource
#from .authentication import CustomAuthentication
#from tastypie.authorization import Authorization

# Create your models here.
class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methodes = ['get']
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'cources'
        allowed_methodes = ['get', 'post', 'delete']
#        authentication = CustomAuthentication()
#        authorization = Authorization()