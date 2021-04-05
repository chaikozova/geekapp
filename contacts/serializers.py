from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('address',
                  'subaddress',
                  'city',
                   'phone_number_o',
                  'phone_number_beeline',
                  'phone_number_megacom',
                  )
       


class QandASerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAndAnswer
        fields = ('id', 'question_text', 'answer_text')

    def create(self, validated_data):
        return QuestionAndAnswer.objects.create(**validated_data)


