from django.urls import path
from . import views

urlpatterns = [
    #
    # API overview of all routes
    path('', views.api_overview, name='api_overview'),
    
    #
    # Student Model Routes
    path('students/list/', views.student_list, name='student_list'),
    path('students/detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:student_id>/', views.student_update, name='student_update'),
    path('students/delete/<int:student_id>/', views.student_delete, name='student_delete'),
    
    #
    # Course Model Routes
    path('courses/list/', views.course_list, name='course_list'),
    path('courses/detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:course_id>/', views.course_update, name='course_update'),
    path('courses/delete/<int:course_id>/', views.course_delete, name='course_delete'),
    
    #
    # Many To Many Relationship Routes Between the Course and Student Models
    path('students/enroll/<int:student_id>/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('students/drop/<int:student_id>/<int:course_id>/', views.drop_course, name='enroll_course'),
]