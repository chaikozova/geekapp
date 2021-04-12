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
        queryset = Request.objects.all()
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            user = request.user
            group = GroupLevel.objects.get(students=user)
            request_month = group.month
            request_teacher = request_month.teacher.first_name + ' ' + request_month.teacher.last_name
            try:
                Request.objects.create(
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
                notification_mentors = User.objects.filter(user_type='MENTOR',
                                                           group_students__level_number__gte=request_month.level_number,
                                                           group_students__level_number__level__title=request_month.course.title).values_list('pk', flat=True)


                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': str(e)})

        return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': serializer.errors.msg})

