from rest_framework import generics
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
