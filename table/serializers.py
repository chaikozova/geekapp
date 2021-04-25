from rest_framework import serializers

from table.models import TableModel


class TableCreateSerializer(serializers.ModelSerializer):
    #date_of_lesson = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = TableModel
        fields = ('id', 'date_of_lesson', 'is_here', 'score')


class TableShowSerializer(serializers.ModelSerializer):
    # student_last_name = serializers.CharField(source='student.last_named')
    # student_first_name = serializers.CharField(source='student.first_name')
    #student = StudentTableSerializer()

    class Meta:
        model = TableModel
        fields = ('id', 'lesson', 'is_here', 'score', 'date_of_lesson')