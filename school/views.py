from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, CourseSerializer
from .models import Student, Course

@api_view(['GET'])
def api_overview(request): # this method just returns an overview of the API routes
    api_urls = {
        'Prod API End Point': 'https://school-backend-v1.herokuapp.com/school/',
        'Dev API End Point': 'http://localhost:8000/school/',
        # Student Model Routes
        'Student List': 'students/list/',
        'Student Detail View': 'students/detail/<int:student_id>/',
        'Student Create': 'students/create/',
        'Student Update': 'students/update/<int:student_id>/',
        'Student Delete': 'students/delete/<int:student_id>',
        # Course Model Routes
        'Course List': 'courses/list/',
        'Course Detail View': 'courses/detail/<int:course_id>/',
        'Course Create': 'courses/create/',
        'Course Update': 'courses/update/<int:course_id>/',
        'Course Delete': 'courses/delete/<int:course_id>',
        # Many-To-Many Relationship Routes Between the Course and Student Models
        'Enroll Student in Course': 'students/enroll/<int:student_id>/<int:course_id>/',
        'Drop Student from Course': 'students/drop/<int:student_id>/<int:course_id>/',
    }
    return Response(api_urls)

#
#
#
# Student Model Routes
# List 
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# Create
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Read
@api_view(['GET'])
def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

# Update
@api_view(['POST'])
def student_update(request, student_id):
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(data=request.data, instance=student)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete
@api_view(['DELETE'])
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({'message': f'{student.first_name} {student.last_name} deleted'})

#
#
#
# Course Model Routes
# List
@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# Create
@api_view(['POST'])
def course_create(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Read
@api_view(['GET'])
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)

# Update
@api_view(['POST'])
def course_update(request, course_id):
    course = Course.objects.get(id=course_id)
    serializer = CourseSerializer(data=request.data, instance=course)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete
@api_view(['DELETE'])
def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return Response({'message': f'{course.first_name} {course.last_name} deleted'})

#
#
#
# Many To Many Relationship Routes Between the Course and Student Models
# Create Relationship
@api_view(['POST'])
def enroll_course(request, student_id, course_id):
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    student.courses.add(course)
    return Response({'message': f'{student.first_name} {student.last_name} enrolled in {course.course_id}'})

# Drop Relationship
@api_view(['POST'])
def drop_course(request, student_id, course_id):
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    student.courses.remove(course)
    return Response({'message': f'{student.first_name} {student.last_name} dropped from {course.course_id}'})