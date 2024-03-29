from firebase_admin import messaging
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from reqs.models import Notification
from reqs.serializers import CreateNotificationSerializer
from users.models import User


def notification_send(req, mentors):
    sender = req.student
    message = req.problem_title
    type = req.category
    registration_tokens = []
    for mentor in mentors:
        print(mentor)
        registration_tokens.append(Token.objects.get(user=mentor))
        notification = Notification.objects.create(
                    recipients=User.objects.get(id=mentor),
                    message=message,
                    type=type,
                    sender=sender)
        notification.save()
        serializer = CreateNotificationSerializer(notification)
    message = messaging.MulticastMessage(
        data={'sender': sender.name, 'type': type, 'message': message},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    print('{0} messages were sent successfully'.format(response.success_count))
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def notification_from_mentor(req):
    sender = req.recipients
    recipients = req.sender
    message = req.message
    type = req.type
    is_read_by_mentor = req.is_read_by_mentor
    try:
        notification = Notification.objects.create(
                recipients=recipients,
                sender=sender,
                message=message,
                type=type,
                is_read_by_mentor=is_read_by_mentor,
        )
        notification.save()
        serializer = CreateNotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'code': status.HTTP_226_IM_USED, 'msg': str(e)})