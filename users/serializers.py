from django.contrib.auth import authenticate
from .models import User, Request
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


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'course',
                  'phone_number', 'telegram', 'instagram', 'github',
                  'is_staff')
        read_only_fields = ('created',)


class TeacherSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)


class UserRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'phone_number', 'telegram', 'instagram', 'github',
                  'image')
        read_only_fields = ('created',)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.image = validated_data.get('image')
        instance.email = validated_data.get('email')
        instance.birthday = validated_data.get('birthday')
        instance.phone_number = validated_data.get('phone_number')
        instance.github = validated_data.get('github')
        instance.instagram = validated_data.get('instagram')
        instance.telegram = validated_data.get('telegram')
        instance.save()
        return instance


class RequestSerializer(serializers.ModelSerializer):
    month = serializers.ChoiceField(choices=Request.MONTH_TYPE)
    category = serializers.ChoiceField(choices=Request.CATEGORY_TYPE)
    course_program = serializers.ChoiceField(choices=Request.PROGRAM_TYPE)
    teacher = serializers.ChoiceField(choices=Request.PROGRAM_TYPE)
    student = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Request
        fields = ('month',
                  'category',
                  'group_number',
                  'course_program',
                  'teacher',
                  'problem_title',
                  'problem_description',
                  'file',
                  'student')

    def create(self, validated_data):
        request = Request.objects.create(
            student=validated_data.get('student', None),
            month=validated_data.get('month', None),
            category=validated_data.get('category', None),
            group_number=validated_data.get('group_number', None),
            course_program=validated_data.get('course_program', None),
            teacher=validated_data.get('teacher', None),
            problem_title=validated_data.get('problem_title', None),
            problem_description=validated_data.get('problem_description', None),
            file=validated_data.get('file', None),
        )
        return request
