from django.http import Http404
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer, LoginSerializer, \
    UserListSerializer, UserRetrieveUpdateDeleteSerializer, RequestSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets, generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Request


class LoginView(APIView):
    """View for log in"""
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'email': user.email,
                         'user_type': user.user_type,
                         'token': token.key}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """View for log out"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        return Response({'success': "Successfully logged out"}, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):
    """View for manager registration"""
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"successful": True}, status=status.HTTP_201_CREATED)
        return Response({"successful": False, **serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = UserRetrieveUpdateDeleteSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        queryset = self.get_object(request.user.pk)
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestAPIView(generics.GenericAPIView,
                     mixins.CreateModelMixin):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
