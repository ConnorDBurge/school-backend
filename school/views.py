# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import Student, Course
# from .forms import StudentForm, CourseForm
# from .serializers import StudentSerializer, CourseSerializer

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# # 
# #
# #
# # Student Routes
# def all_students(request):
#     students = Student.objects.all()
#     serialized_students = StudentSerializer(students).all_students
#     return JsonResponse(data=serialized_students, status=200)

# def detail_student(request, student_id):
#     student = Student.objects.get(id=student_id)
#     serialized_student = StudentSerializer(student).detail_student
#     return JsonResponse(data=serialized_student, status=200)

# @csrf_exempt
# def new_student(request):
#     if request.method == 'POST':
#         data = json.load(request)
#         form = StudentForm(data)
#         if form.is_valid():
#             student = form.save(commit=True)
#             serialized_student = StudentSerializer(student).detail_student
#             return JsonResponse(data=serialized_student, status=200)

# @csrf_exempt
# def edit_student(request, student_id):
#     student = Student.objects.get(id=student_id)
#     if request.method == 'POST':
#         data = json.load(request)
#         form = StudentForm(data, instance=student)
#         if form.is_valid():
#             student = form.save(commit=True)
#             serialized_student = StudentSerializer(student).detail_student
#             return JsonResponse(data=serialized_student, status=200)

# @csrf_exempt
# def delete_student(request, student_id):
#     student = Student.objects.get(id=student_id)
#     student.delete()
#     return JsonResponse(data={'message': 'Student deleted'}, status=200)        

# #
# #
# #
# # Course Routes
# def all_courses(request):
#     courses = Course.objects.all()
#     serialized_courses = CourseSerializer(courses).all_courses
#     return JsonResponse(data=serialized_courses, status=200)

# def detail_course(request, course_id):
#     course = Course.objects.get(id=course_id)
#     serialized_course = CourseSerializer(course).detail_course
#     return JsonResponse(data=serialized_course, status=200)

# @csrf_exempt
# def new_course(request):
#     if request.method == 'POST':
#         data = json.load(request)
#         form = CourseForm(data)
#         if form.is_valid():
#             course = form.save(commit=True)
#             serialized_course = CourseSerializer(course).detail_course
#             return JsonResponse(data=serialized_course, status=200)
        
# @csrf_exempt
# def edit_course(request, course_id):
#     course = Course.objects.get(id=course_id)
#     if request.method == 'POST':
#         data = json.load(request)
#         form = CourseForm(data, instance=course)
#         if form.is_valid():
#             course = form.save(commit=True)
#             serialized_course = CourseSerializer(course).detail_course
#             return JsonResponse(data=serialized_course, status=200)
        
# @csrf_exempt
# def delete_course(request, course_id):
#     course = Course.objects.get(id=course_id)
#     course.delete()
#     return JsonResponse(data={'message': 'Course deleted'}, status=200)  

# @csrf_exempt
# def enroll_student(request, course_id, student_id):
#     course = Course.objects.get(id=course_id)
#     student = Student.objects.get(id=student_id)
#     course.students.add(student)
#     return JsonResponse(data={'message': f'{student.first_name} {student.last_name} enrolled in {course.course_name}'}, status=200)

# @csrf_exempt
# def drop_student(request, course_id, student_id):
#     course = Course.objects.get(id=course_id)
#     student = Student.objects.get(id=student_id)
#     course.students.remove(student)
#     return JsonResponse(data={'message': f'{student.first_name} {student.last_name} dropped from {course.course_name}'}, status=200)