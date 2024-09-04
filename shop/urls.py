from django.urls import path
from . import views

app_name =  'shop'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course')

    # запись ниже может быть корректа использована с кодом: <td><a href={% url "shop:single_course" course.id %}>{{course.title}}</a></td>
    # path('course/<int:course_id>', views.single_course, name='single_course')
]