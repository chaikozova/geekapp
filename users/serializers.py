from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from table.serializers import TableShowSerializer
from .mentor_comment import MentorComment
from .models import User, IsMentor
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(label='password',
                                     style={'input_type': 'password'},
                                     write_only=True,
                                     trim_whitespace=False)
    token = serializers.CharField(label='token', read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email',
                  'password',
                  'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            is_active=True,
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'password': 'Old password is not correct.'})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UserListSerializer(serializers.ModelSerializer):
    # courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'coins',
                  'phone_number', 'telegram', 'instagram', 'github',
                  'is_staff')


class UserShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image')


class StudentTableSerializer(serializers.ModelSerializer):
    table_student = TableShowSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'table_student')


class TeacherSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)


class UserRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'telegram',
                  'github', 'instagram', 'image', 'phone_number', 'birthday')
        read_only_fields = ('user_type',)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.telegram = validated_data.get('telegram')
        instance.github = validated_data.get('github')
        instance.instagram = validated_data.get('instagram')
        instance.image = validated_data.get('image')
        instance.phone_number = validated_data.get('phone_number')
        instance.birthday = validated_data.get('birthday')
        instance.save()
        return instance


class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image',)


class EmailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class MentorCommentSerializer(serializers.ModelSerializer):
    mentor = UserShortInfoSerializer(read_only=True)
    user = UserShortInfoSerializer(read_only=True, many=True)
    created = serializers.DateTimeField(format="%d.%m.%Y - %H:%M:%S")

    class Meta:
        model = MentorComment
        fields = ('id', 'comment', 'created', 'rate', 'users', 'mentor')
        read_only_fields = ('created', )


class UserMainInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birthday', 'phone_number')


class UserSocialMediaInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('github', 'telegram', 'instagram')


class IsMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsMentor
        fields = ('user',
                  'is_mentor',
                  'blank_to_be_mentor')
