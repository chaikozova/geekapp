from rest_framework import generics
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactAPIView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


