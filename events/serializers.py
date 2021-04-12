from decimal import Decimal

from django.db.models import Avg
from rest_framework import serializers
from events.models import Event, Comment
from users.models import User
from users.serializers import UserShortInfoSerializer


class CommentSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    user = UserShortInfoSerializer(read_only=True)
    #created = serializers.DateTimeField(format="%d.%m.%Y - %H:%M:%S")

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'rate', 'events', 'user')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


    # def update(self, instance, validated_data):
    #     instance.comment = validated_data.get('comment')
    #     instance.created = validated_data.get('created')
    #     return instance


class EventSerializer(serializers.ModelSerializer):
    #date_of_event = serializers.DateTimeField(format="%d.%m.%Y - %H:%M:%S")

    class Meta:
        model = Event
        fields = ('id', 'title', 'date_of_event', 'time_of_event', 'rating_average', 'image')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     comments_data = validated_data.pop('comments')
    #     comments = instance.comments
        # instance.image = validated_data.get('image')
        # instance.title = validated_data.get('title')
        # instance.description = validated_data.get('description')
        # instance.created = validated_data.get('created')
        # instance.date_of_event = validated_data.get('date_of_event')
        # instance.location = validated_data.get('location')
        # instance.save()
        # for comments_data in comments_data:
        #     comment = comments.pop(0)
        #     comment.comment = comments_data.get('comment')
        #     comment.created = comments_data.get('created')
        #     comment.save()
        # return instance


class EventDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    #date_of_event = serializers.DateTimeField(format="%d.%m.%Y - %H:%M:%S")

    class Meta:
        model = Event
        fields = ('id', 'image', 'title', 'description', 'rating_average',
                  'date_of_event', 'time_of_event', 'location', 'dop_location', 'user', 'comments')