from rest_framework import generics
from contacts.models import ToJoinTheCourse
from contacts.serializers import ToJoinTheCourseSerializer


class ToJoinTheCourseAPIView(generics.ListCreateAPIView):
    serializer_class = ToJoinTheCourseSerializer
    queryset = ToJoinTheCourse.objects.all()
