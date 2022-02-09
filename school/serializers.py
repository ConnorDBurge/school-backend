from rest_framework import serializers
from .models import Student, Course
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_id', 'course_name', 'students']
        depth = 1
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'courses']
        depth = 1