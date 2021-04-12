from rest_framework import generics
from contacts.models import Contact, ToJoinTheCourse
from contacts.serializers import ContactSerializer, ToJoinTheCourseSerializer


class ContactAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ToJoinTheCourseAPIView(generics.ListCreateAPIView):
    serializer_class = ToJoinTheCourseSerializer
    queryset = ToJoinTheCourse.objects.all()
