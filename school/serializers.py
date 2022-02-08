from rest_framework import serializers
from .models import Student, Course
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        depth = 1
        
class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1