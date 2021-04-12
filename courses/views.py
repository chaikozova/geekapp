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

    def get_queryset(self):
        course = self.kwargs['id']
        return Level.objects.filter(course_id=course)


class LevelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LevelDetailSerializer

    def get_queryset(self):
        course_id = self.kwargs['id']
        level_id = self.kwargs['pk']
        return Level.objects.filter(pk=level_id, course_id=course_id)


class LessonAPIView(generics.ListCreateAPIView):
    """
    List of lessons in 1 month
    """
    serializer_class = LessonSerializer

    def get_queryset(self):
        level = self.kwargs['pk']
        return Lesson.objects.filter(level_id=level)


class LessonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonDetailSerializer

    def get_queryset(self):
        level = self.kwargs['pk']
        lesson_id = self.kwargs['i']
        return Lesson.objects.filter(pk=lesson_id, level_id=level)

