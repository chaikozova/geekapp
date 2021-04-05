from rest_framework import serializers

from contacts.models import Contact, QuestionAndAnswer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('address',
                  'subaddress',
                  'city',
                  'phone_number',
                  'url')


class QandASerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAndAnswer
        fields = ('id', 'question_text', 'answer_text')

    def create(self, validated_data):
        return QuestionAndAnswer.objects.create(**validated_data)

