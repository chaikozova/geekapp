from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Course, Level, Lesson, GroupLevel
from courses.serializers import CourseSerializer, LevelDetailSerializer, LessonSerializer, CourseDetailSerializer, \
    LessonDetailSerializer, LevelSerializer, GroupStudentsListSerializers


class CourseAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'


class CourseDetailAPIView(generics.RetrieveUpdateAPIView):
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


class LessonDetailAPIView(APIView):

    def get(self, request, course_id, level_id, lesson_id):
        serializer_class = LessonDetailSerializer
        try:
            course = Course.objects.get(id=course_id)
            level = Level.objects.get(pk=level_id, course=course)
            lesson = Lesson.objects.get(id=lesson_id, level=level)
            serializers = serializer_class(lesson)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': str(e)})


class ListOfGroupsSerializer(APIView):

    def get(self, request):
        serializer_class = GroupStudentsListSerializers
        groups = GroupLevel.objects.all()
        return Response(data=serializer_class(groups, many=True).data, status=status.HTTP_200_OK)
