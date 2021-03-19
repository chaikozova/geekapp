from rest_framework import generics

from courses.models import Course, Level, Lesson
from courses.serializers import CourseSerializer, LevelSerializer, LessonSerializer


class CourseAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'


class LevelAPIView(generics.ListCreateAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = "id"


class LevelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = "id"


class LessonAPIView(generics.ListCreateAPIView):
    """
    List of lessons in 1 month
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'id'
