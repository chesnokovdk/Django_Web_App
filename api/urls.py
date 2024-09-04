from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
# course_resource = CourseResource()
# category_resource = CategoryResource()
api.register(CourseResource())
api.register(CategoryResource())

# api/v1/cources/         GET, POST
# api/v1/cources/1/       GET, DELETE
# api/v1/categories/      GET
# api/v1/ccategories/1/   GET

# For POST, DELETE add heafer
# Key: Authorization
# Value: ApiKey qwe:qwe123

urlpatterns = [
    path('',include(api.urls), name='index')

]