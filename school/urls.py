from django.urls import path
from . import views

urlpatterns = [
    # Student routes
    path('students', views.all_students, name='all_students'),
    path('students/new', views.new_student, name='new_student'),
    path('students/<int:student_id>', views.detail_student, name='detail_student'),
    path('students/<int:student_id>/edit', views.edit_student, name='edit_student'),
    path('students/<int:student_id>/delete', views.delete_student, name='delete_student'),
    # Course routes
    path('courses', views.all_courses, name='all_courses'),
    path('courses/new', views.new_course, name='new_course'),
    path('courses/<int:course_id>', views.detail_course, name='detail_course'),
    path('courses/<int:course_id>/enroll-student/<int:student_id>', views.enroll_student, name='enroll_student'),
    path('courses/<int:course_id>/drop-student/<int:student_id>', views.drop_student, name='drop_student'),
    path('courses/<int:course_id>/edit', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete', views.delete_course, name='delete_course'),
]