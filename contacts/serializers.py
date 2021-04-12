
from rest_framework import serializers
from contacts.models import Contact, ToJoinTheCourse


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


class ToJoinTheCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToJoinTheCourse
        fields = ('course',
                  'name_and_surname',
                  'telephone_number',
                  )