from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Room
from chat.serializers import RoomSerializer
from requests.models import Request, Notification
from requests.notification_create import notification_send, notification_from_mentor
from requests.serializers import CreateRequestSerializer, CreateNotificationSerializer
from courses.models import GroupLevel


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
                notification_send(req, req.notification_mentors)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'code': status.HTTP_226_IM_USED, 'msg': str(e)})
        return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': serializer.errors})


class MentorResponseToRequestAPIView(APIView):
    serializer_class = CreateNotificationSerializer

    def put(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.is_read_by_mentor = True
        notification.save()
        notification_from_mentor(notification)
        serializer = self.serializer_class(notification)
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)


class CreateRoomForMentorAndStudentAPIView(APIView):

    def put(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.is_match = True
        notification.save()

        if notification.is_match and notification.is_read_by_mentor:
            room = Room.objects.create(creator=notification.recipients)
            room.invited.add(notification.sender)
            room.save()
            return Response(data=RoomSerializer(room).data,
                            status=status.HTTP_201_CREATED)
        elif not notification.is_match:
            notification.delete()
            return Response({'code': status.HTTP_200_OK, 'msg': 'Request has been deleted.'})
        return Response({'code': status.HTTP_400_BAD_REQUEST})


class NotificationsAPIView(APIView):
    serializer_class = CreateNotificationSerializer

    def get(self, request):
        notification = Notification.objects.filter(recipients=request.user)
        serializers = self.serializer_class(notification, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
