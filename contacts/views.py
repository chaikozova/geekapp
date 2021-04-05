from rest_framework import generics
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework.views import APIView
from contacts.models import Contact, QuestionAndAnswer
from contacts.serializers import ContactSerializer, QandASerializer


class ContactAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class QandAAPIView(generics.ListCreateAPIView):
    serializer_class = QandASerializer
    queryset = QuestionAndAnswer.objects.all()
    lookup_field = 'id'
