from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Room
from chat.serializers import RoomListSerializer, RoomSerializer
from reqs.models import Request, Notification
from reqs.notification_create import notification_send, notification_from_mentor
from reqs.serializers import CreateRequestSerializer, CreateNotificationSerializer, NotificationListSerializer
from courses.models import GroupLevel
from users.models import User


class CreateRequestMentorHelpAPIView(APIView):
    serializer_class = CreateRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            group = GroupLevel.objects.get(students=user)
            request_month = group.month
            course = request_month.course
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
                mentors = User.objects.filter(user_type='MENTOR',
                                              group_students__month__course=course,
                                              group_students__month__level_number__gt=request_month.level_number)
                mentors = mentors.values_list('id', flat=True)
                print(mentors)
                notification_send(req, mentors)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'code': status.HTTP_226_IM_USED, 'msg': str(e)})
        return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': serializer.errors})


class MentorResponseToRequestAPIView(APIView):
    serializer_class = CreateNotificationSerializer

    def put(self, request, id):
        notification = Notification.objects.get(id=id, recipients=request.user)
        notification.is_read_by_mentor = True
        notification.save()
        notification_from_mentor(notification)
        serializer = self.serializer_class(notification)
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.delete()
        serializer = self.serializer_class(notification)
        return Response({'msg': 'Notification has been deleted.'})


class CreateRoomForMentorAndStudentAPIView(APIView):

    def put(self, request, id):
        notification = Notification.objects.get(id=id, recipients=request.user)
        notification.is_match = True
        notification.save()

        if notification.is_match and notification.is_read_by_mentor:
            room = Room.objects.create(creator=notification.recipients,
                                       name=notification.message)
            room.invited.add(notification.sender)
            room.save()
            notification.delete()
            return Response(data=RoomSerializer(room).data,
                            status=status.HTTP_201_CREATED)
        elif not notification.is_match:
            notification.delete()
            return Response({'code': status.HTTP_200_OK, 'msg': 'Request has been deleted.'})
        return Response({'code': status.HTTP_400_BAD_REQUEST})


class StudentRejectNotificationAPIView(APIView):
    serializer_class = NotificationListSerializer

    def delete(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.is_match = False
        notification.delete()
        serializers = self.serializer_class(notification)
        return Response({'msg': 'Notification has been deleted.'})


class NotificationsListAPIView(APIView):
    serializer_class = NotificationListSerializer

    def get(self, request):
        notifications = Notification.objects.filter(recipients=request.user)
        serializers = self.serializer_class(notifications, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class MyNotificationsAPIView(APIView):
    serializer_class = RoomListSerializer

    def get(self, request):
        chats = Room.objects.filter(invited=request.user)
        serializers = self.serializer_class(chats, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class MyRequestsAPIView(APIView):
    serializer_class = RoomListSerializer

    def get(self, request):
        chats = Room.objects.filter(creator=request.user)
        serializers = self.serializer_class(chats, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class EndTheRoomAPIView(APIView):
    serializer_class = RoomListSerializer

    def delete(self, request, id):
        room = Room.objects.get(id=id)
        student = room.creator
        mentors = room.invited.all()
        student.coins -= 1
        student.save()
        mentor = mentors[0]
        mentor.coins += 1
        mentor.save()
        room.delete()
        return Response({'msg': 'The chat has been deleted.'})