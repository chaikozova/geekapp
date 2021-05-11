from django.contrib.auth import authenticate
from django.http import Http404
from fcm_django.models import FCMDevice
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from .mentor_comment import MentorComment
from .serializers import UserRegistrationSerializer, LoginSerializer, \
    UserListSerializer, UserRetrieveUpdateDeleteSerializer, ChangePasswordSerializer, \
    MentorCommentSerializer, EmailUpdateSerializer, ImageUpdateSerializer, UserMainInfoUpdateSerializer, \
    UserSocialMediaInfoUpdateSerializer, IsMentorSerializer, UserShortInfoSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, IsMentor


class LoginView(APIView):
    """View for log in"""
    serializer_class = LoginSerializer

    def post(self, request):
        global device
        fcm = request.data.get("fcm_token")
        user = authenticate(email=request.data.get("email"),
                            password=request.data.get("password"))
        if user is not None:
            ser = UserShortInfoSerializer(user)
            fb = User.objects.get(id=user.id)
            print(ser.data['id'])
            try:
                devices = FCMDevice.objects.get(user=ser.data['id'])
            except FCMDevice.DoesNotExist:
                devices = None
            if devices is None:
                device = FCMDevice()
                device.user = user
                device.registration_id = fcm
                device.type = "Android"
                device.name = "Can be anything"
                device.save()
            else:
                devices.registration_id = fcm
                devices.save()
            try:
                token = Token.objects.get(user_id=user.id)
            except:
                token = Token.objects.create(user=user)
                print(token.key)
                print(user)

            return Response({
                "token": token.key,
                "device_id": device.registration_id,
                "error": False
                             })
        else:
            data = {
                "error": True,
                "msg": "User does not exist or password is wrong"
            }

            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


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
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                fcm_token = json['fcm_token']
                user = json['id']
                device = FCMDevice()
                device.registration_id = fcm_token
                device.type = "Android"
                device.name = "Can be anything"
                device.user = user
                device.save()
                return Response(
                    {
                        "token": token.key,
                        "device_id": device.registration_id,
                        "error": False
                    }, status=status.HTTP_201_CREATED)
            else:
                data = {"error": True, "errors": serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    """
    View for password reset
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer


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
        return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': serializer.errors})


class MentorCommentsView(APIView):
    """
    Mentor comments view which is available for many others users for comment.
    """
    serializer_class = MentorCommentSerializer
    queryset = MentorComment.objects.all()
    lookup_field = 'id'


class ImageUpdateView(GenericAPIView, UpdateModelMixin):
    serializer_class = ImageUpdateSerializer

    def get_queryset(self):
        image_id = self.kwargs['pk']
        return User.objects.get(pk=image_id)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EmailUpdateView(generics.UpdateAPIView):
    serializer_class = EmailUpdateSerializer

    def get_queryset(self):
        email_id = self.kwargs['pk']
        return User.objects.get(pk=email_id)


class UserMainInfoUpdateView(generics.UpdateAPIView):
    serializer_class = UserMainInfoUpdateSerializer

    def get_queryset(self):
        email_id = self.kwargs['pk']
        return User.objects.get(pk=email_id)


class UserSocialInfoUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSocialMediaInfoUpdateSerializer

    def get_queryset(self):
        email_id = self.kwargs['pk']
        return User.objects.get(pk=email_id)


class IsMentorView(generics.CreateAPIView):
    serializer_class = IsMentorSerializer
    queryset = IsMentor.objects.all()
