from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from requests.models import Request
from requests.serializers import CreateRequestSerializer
from courses.models import GroupLevel
from users.models import User


class CreateRequestMentorHelpAPIView(APIView):
    serializer_class = CreateRequestSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            group = GroupLevel.objects.get(students=user)
            request_month = group.month
            request_teacher = request_month.teacher.first_name + ' ' + request_month.teacher.last_name
            try:
                req = Request.objects.create(
                    student=user,
                    month=request_month.level_number,
                    category=serializer.data['category'],
                    group_number=group.name,
                    course_program=request_month.course.title,
                    teacher=request_teacher,
                    problem_title=serializer.data['problem_title'],
                    problem_description=serializer.data['problem_description'],
                    file=serializer.data['file']
                )
                req.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'code': status.HTTP_226_IM_USED, 'msg': str(e)})
        return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': serializer.errors.msg})

