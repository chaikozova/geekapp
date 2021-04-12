from .models import Request
from rest_framework import serializers


class CreateRequestSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Request.CATEGORY_TYPE)

    class Meta:
        model = Request
        fields = (
            # 'month',
            'category',
            # 'group_number',
            # 'course_program',
            # 'teacher',
            'problem_title',
            'problem_description',
            'file',
            # 'student'
        )

    # def create(self, validated_data):
    #     request = Request.objects.create(
    #         student=validated_data.get('student', None),
    #         month=validated_data.get('month', None),
    #         category=validated_data.get('category', None),
    #         group_number=validated_data.get('group_number', None),
    #         course_program=validated_data.get('course_program', None),
    #         teacher=validated_data.get('teacher', None),
    #         problem_title=validated_data.get('problem_title', None),
    #         problem_description=validated_data.get('problem_description', None),
    #         file=validated_data.get('file', None),
    #     )
    #     return request