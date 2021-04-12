
from rest_framework import serializers
from contacts.models import ToJoinTheCourse



class ToJoinTheCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToJoinTheCourse
        fields = ('course',
                  'name_and_surname',
                  'telephone_number',
                  )
