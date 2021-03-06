from rest_framework import serializers

from courses.models import Course, Level, Lesson, GroupLevel
from users.models import User
from users.serializers import TeacherSerializer, UserShortInfoSerializer, StudentTableSerializer


class LessonDetailSerializer(serializers.ModelSerializer):
    level = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())

    class Meta:
        model = Lesson
        fields = ('level', 'id', 'title', 'description', 'video_url', 'material_url', 'homework',)

    def create(self, validated_data):
        return Lesson.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     return instance


class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('id', 'title',)


class LevelDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Level
        fields = ('id', 'title', 'image', 'teacher', 'lessons')

    # def create(self, validated_data):
    #     lesson_data = validated_data.pop('lessons')
    #     teacher_data = validated_data.pop('teacher')
    #     teacher = Users.objects.get_or_create()
    #     Lesson.objects.create(level=level, teacher=teacher, **lesson_data)
    #
    #     return level
    #
    def update(self, instance, validated_data):
        lesson_data = validated_data.pop('lessons')
        lessons = instance.lessons

        instance.title = validated_data.get('title')
        instance.image = validated_data.get('image')
        instance.teacher = validated_data.get('teacher')
        instance.save()
        for lesson_data in lesson_data:
            lesson = lessons.pop(0)
            lesson.title = lesson_data.get('title')
            lesson.description = lesson_data.get('description')
            lesson.video_url = lesson_data.get('video_url')
            lesson.material_url = lesson_data.get('material_url')
            lesson.save()

        return instance


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'title',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'logo', 'color', 'title')


class CourseDetailSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=False, many=True)

    class Meta:
        model = Course
        fields = ('id', 'logo', 'title', 'description', 'level')

    def update(self, instance, validated_data):
        level_data = validated_data.pop('level')
        levels = instance.level.all()
        levels = list(levels)
        instance.logo = validated_data.get('logo')
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.color = validated_data.get('color')
        instance.save()

        for level_data in level_data:
            level1 = levels.pop(0)
            level1.title = level_data.get('title')
            level1.teacher = level_data.get('teacher')
            level1.image = level_data.get('image')
            level1.save()
        return instance


class GroupNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupLevel
        fields = ('id', 'name',)


class GroupStudentsListSerializers(serializers.ModelSerializer):
    student_last_name = serializers.CharField(source='students.last_name')
    student_first_name = serializers.CharField(source='students.first_name')
    group_students = StudentTableSerializer(many=True, read_only=True)

    class Meta:
        model = GroupLevel
        fields = ('id', 'name', 'group_students', 'student_first_name', 'student_last_name' )


class GroupTableListSerializers(serializers.ModelSerializer):

    group_students = StudentTableSerializer(read_only=True, many=True)

    class Meta:
        model = GroupLevel
        fields = ('id', 'name', 'group_students', )

