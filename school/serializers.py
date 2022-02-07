# from builtins import object
from rest_framework import serializers
from .models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'courses']
        depth = 1
        
class CourseSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'course_id', 'course_name', 'students']
        depth = 1


# class StudentSerializer(object):
#     def __init__(self, data):
#         self.data = data # init with a QuerySet

#     @property
#     def all_students(self):
#         output = {'students': []}
#         for student in self.data:
#             student_data = {
#                 'first_name': student.first_name,
#                 'last_name': student.last_name,
#                 'courses': CourseSerializer(student.courses.all()).student_courses
#             }
#             output['students'].append(student_data)
#         return output
    
#     @property
#     def detail_student(self):
#         return {
#                 'first_name': self.data.first_name,
#                 'last_name': self.data.last_name,
#                 'courses': CourseSerializer(self.data.courses.all()).student_courses
#             }
        
#     @property
#     def course_students(self):
#         output = []
#         for student in self.data:
#             student_data = {
#                 'first_name': student.first_name,
#                 'last_name': student.last_name
#             }
#             output.append(student_data)
#         return output
        
# class CourseSerializer(object):
#     def __init__(self, data):
#         self.data = data

#     @property
#     def all_courses(self):
#         output = {'courses': []}
#         for course in self.data:
#             course_data = {
#                 'course_id': course.course_id,
#                 'course_name': course.course_name, 
#                 'students': StudentSerializer(course.students.all()).course_students
#             }
#             output['courses'].append(course_data)
#         return output
        
#     @property
#     def detail_course(self):
#         return {
#                 'course_id': self.data.course_id,
#                 'course_name': self.data.course_name,
#                 'students': StudentSerializer(self.data.students.all()).course_students
#             }
        
#     @property
#     def student_courses(self):
#         output = []
#         for course in self.data:
#             course_data = {
#                 'course_id': course.course_id,
#                 'course_name': course.course_name, 
#             }
#             output.append(course_data)
#         return output