from rest_framework import generics
from contacts.models import Contact, ToJoinTheCourse, QuestionAndAnswer
from contacts.serializers import ContactSerializer, ToJoinTheCourseSerializer, QandASerializer


class ContactAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ToJoinTheCourseAPIView(generics.ListCreateAPIView):
    serializer_class = ToJoinTheCourseSerializer
    queryset = ToJoinTheCourse.objects.all()


class QandAAPIView(generics.ListCreateAPIView):
    serializer_class = QandASerializer
    queryset = QuestionAndAnswer.objects.all()
    lookup_field = 'id'
