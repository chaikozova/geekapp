from rest_framework import generics

from courses.models import Course, Level, Lesson
from courses.serializers import CourseSerializer, LevelDetailSerializer, LessonSerializer, CourseDetailSerializer, \
    LessonDetailSerializer, LevelSerializer


class CourseAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'


class LevelAPIView(generics.ListCreateAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = "id"


class LevelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LevelDetailSerializer
    queryset = Level.objects.all()
    lookup_field = "id"


class LessonAPIView(generics.ListCreateAPIView):
    """
    List of lessons in 1 month
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'id'


class LessonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'id'
