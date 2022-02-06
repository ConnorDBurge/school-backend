from django.forms import ModelForm
from .models import Student, Course

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name')
        
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name')