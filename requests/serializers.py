from .models import Request, Notification
from rest_framework import serializers


class CreateRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = (
            'id',
            'category',
            'problem_title',
            'problem_description',
            'file',
        )


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = (
            'id',
            'student',
            'month',
            'group_number',
            'category',
            'course_program',
            'teacher',
            'problem_title',
            'problem_description',
            'file',
        )

class CreateNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = (
            'id',
            'message',
            'type',
            'recipients',
            'sender',
        )


class NotificationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = (
            'id',
            'message',
            'type',
            'recipients',
            'sender',
            'recieved_date',
            'created',
        )