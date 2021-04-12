from .models import Request
from rest_framework import serializers


class CreateRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = (
            'category',
            'problem_title',
            'problem_description',
            'file',
        )
