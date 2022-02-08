from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, CourseSerializer
from .models import Student, Course

@api_view(['GET'])
def api_overview(request): # this method just returns an overview of the API routes
    api_urls = {
        'Student List': 'students/list/',
        'Student Detail View': 'students/detail/<int:student_id>/',
        'Student Create': 'students/create/',
        'Student Update': 'students/update/<int:student_id>/',
        'Student Delete': 'students/delete/<int:student_id>',
        'Course List': 'courses/list/',
        'Course Detail View': 'courses/detail/<int:courses_id>/',
        'Course Create': 'courses/create/',
        'Course Update': 'courses/update/<int:courses_id>/',
        'Course Delete': 'courses/delete/<int:courses_id>'
    }
    return Response(api_urls)

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def student_update(request, student_id):
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(data=request.data, instance=student)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({'message': f'{student.first_name} {student.last_name} deleted'})

@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def course_create(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def course_update(request, course_id):
    course = Course.objects.get(id=course_id)
    serializer = CourseSerializer(data=request.data, instance=course)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return Response({'message': f'{course.first_name} {course.last_name} deleted'})