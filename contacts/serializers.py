from rest_framework import serializers
from contacts.models import Contact, ToJoinTheCourse, QuestionAndAnswer




class QandASerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAndAnswer
        fields = ('id', 'question_text', 'answer_text')

    def create(self, validated_data):
        return QuestionAndAnswer.objects.create(**validated_data)


class ToJoinTheCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToJoinTheCourse
        fields = ('course',
                  'name_and_surname',
                  'telephone_number',
                  )
