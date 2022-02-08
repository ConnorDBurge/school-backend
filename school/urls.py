from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    
    path('students/list/', views.student_list, name='student_list'),
    path('students/detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:student_id>/', views.student_update, name='student_update'),
    path('students/delete/<int:student_id>/', views.student_delete, name='student_delete'),
    
    path('courses/list/', views.course_list, name='course_list'),
    path('courses/detail/<int:courses_id>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:courses_id>/', views.course_update, name='course_update'),
    path('courses/delete/<int:courses_id>/', views.course_delete, name='course_delete'),
]