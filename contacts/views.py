from rest_framework import generics
from rest_framework.views import APIView

from contacts.models import Contact, QuestionAndAnswer
from contacts.serializers import ContactSerializer, QandASerializer


class ContactAPIView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QandAAPIView(generics.ListCreateAPIView):
    serializer_class = QandASerializer
    queryset = QuestionAndAnswer.objects.all()
    lookup_field = 'id'


