from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import GroupLevel, Lesson
from courses.serializers import GroupStudentsListSerializers, GroupTableListSerializers
from table.models import TableModel
from table.serializers import TableCreateSerializer, TableShowSerializer
from users.models import User
from users.serializers import StudentTableSerializer


class TableCreateAPIView(APIView):
    serializer_class = TableCreateSerializer

    def post(self, request, lesson_id, student_id):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            student = get_object_or_404(User, id=student_id)
            lesson = get_object_or_404(Lesson, id=lesson_id)
            try:
                table = TableModel.objects.create(
                    student=student,
                    lesson=lesson,
                    date_of_lesson=serializers.data['date_of_lesson'],
                    is_here=serializers.data['is_here'],
                )
                table.save()
                return Response(data=TableCreateSerializer(table).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'code': status.HTTP_400_BAD_REQUEST,
                                 'msg': str(e)})

    def get(self, request, group_id):
        try:
            group = GroupLevel.objects.get(id=group_id)
            serializers = GroupStudentsListSerializers(group)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': str(e)})


class TableShowAPIView(APIView):
    serializer_class = TableShowSerializer

    def get(self, request, group_id):
        try:
            group = GroupLevel.objects.get(id=group_id)
            student = User.objects.get(group_students=group)
            student_table = StudentTableSerializer(student)
            return Response(data=student_table.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': str(e)})
