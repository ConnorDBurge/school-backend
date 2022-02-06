from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    course_id = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name="courses")
    
    def __str__(self):
        return f'{self.course_id}: {self.course_name}'
